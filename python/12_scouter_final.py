import streamlit as st
import requests
from bs4 import BeautifulSoup
import joblib
import numpy as np

# =============================================================================
# BLOQUE 1: EL CEREBRO
# =============================================================================

# TU RETO: Carga el modelo .pkl que ya conoces.
modelo = joblib.load("10_modelo_scouting.pkl")

# =============================================================================
# BLOQUE 2: LA ENTRADA (SCRAPING)
# =============================================================================

st.title("🕵️‍♂️ Buscador de Talento Automático")
url = st.text_input("Pega la URL de LaLiga del jugador:")

if st.button("Analizar Perfil"):
    if url:
        # Configuración para evitar bloqueos
        headers = {"User-Agent": "Mozilla/5.0"}

        # TU RETO: Realiza la petición y crea el objeto BeautifulSoup.
        # Pista: Reutiliza tu código del Ejercicio 5.
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")

        try:
            # 1. EXTRAER NOMBRE
            # Pista: Busca el <strong> dentro de la cabecera.
            nombre = soup.select(".playerInfo h1")[0].text.strip()

            # 2. EXTRAER ESTADÍSTICAS (El reto rebelde)
            # Transfermarkt es complejo. Para este ejercicio final, vamos a
            # buscar los datos en las etiquetas de 'puntos' o 'stats'.
            # Pista: Si se te complica el selector, busca el texto "Goles" o "Asistencias".
            # Por ahora, puedes simular la extracción o intentar el selector:
            # soup.find_all("span", class_="items__item-main")

            # Supongamos que tras limpiar el texto obtienes:
            goles_extraidos = int(
                soup.select(
                    ".styled__StatsRow-sc-19ye3lp-2 div div div p:nth-child(1)"
                )[0].text.strip()
            )  # Sustituye por tu lógica de scraping
            asistencias_extraidas = int(
                soup.select(
                    ".styled__StatsRow-sc-19ye3lp-2 div div div p:nth-child(1)"
                )[1].text.strip()
            )  # Sustituye por tu lógica de scraping

            # =================================================================
            # BLOQUE 3: EL VEREDICTO DE LA IA
            # =================================================================

            # TU RETO: Pasa los datos extraídos por el modelo.
            # Pista: Recuerda el formato array 2D [[goles, asistencias]].
            datos = np.array([[goles_extraidos, asistencias_extraidas]])
            prediccion = modelo.predict(datos)

            # INTERFAZ FINAL
            st.divider()
            st.header(nombre)

            col1, col2 = st.columns(2)
            col1.metric("Goles", goles_extraidos)
            col2.metric("Asistencias", asistencias_extraidas)

            # TU RETO: Muestra si es Estrella o Relleno según la predicción.
            # Pista: if prediccion == 1: ...
            if prediccion:
                st.success("El jugador es una estrella")
            else:
                st.info("El jugador es uno del montón")

        except Exception as e:
            st.error(f"Error al leer el perfil: {e}")
    else:
        st.warning("Por favor, introduce una URL válida.")
