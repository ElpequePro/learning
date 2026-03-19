import streamlit as st
import joblib
import numpy as np

# =============================================================================
# BLOQUE 1: CONFIGURACIÓN Y CARGA
# Objetivo: Preparar la interfaz y despertar el "cerebro" de la IA.
# =============================================================================

st.title("⚽ Panel de Control: Scouting Inteligente")
st.write("Bienvenido, Director Deportivo. Introduce los datos del candidato.")

# TU RETO: Carga el modelo que guardaste en el ejercicio 10.
# Pista: usa joblib.load con el nombre exacto del archivo (.pkl).
modelo = joblib.load("10_modelo_scouting.pkl")

# =============================================================================
# BLOQUE 2: ENTRADA DE DATOS (INTERFAZ)
# Objetivo: Crear los controles para que el usuario interactúe.
# =============================================================================

st.write("### Estadísticas de la Temporada")

# TU RETO: Crea dos sliders (barras) para Goles y Asistencias.
# Pista: st.slider("Etiqueta", min_val, max_val, valor_inicial)
goles = st.slider("Goles", 0, 30, 5)
asistencias = st.slider("Asistencias", 0, 20, 3)

# =============================================================================
# BLOQUE 3: LÓGICA DE PREDICCIÓN
# Objetivo: Que la IA analice los datos al pulsar el botón.
# =============================================================================

if st.button("Ejecutar Análisis"):
    # 1. Preparar los datos
    # TU RETO: Convierte los valores de los sliders en un array de numpy 2D.
    # Pista: recuerda los corchetes dobles [[goles, asistencias]].
    datos_jugador = np.array([[goles, asistencias]])

    # 2. Realizar la predicción
    # TU RETO: Usa el método predict del modelo cargado.
    prediccion = modelo.predict(datos_jugador)

    # 3. Mostrar resultados
    st.write("---")
    # TU RETO: Si la predicción es 1, muestra un mensaje de éxito (estrella).
    # Si es 0, muestra un mensaje informativo (relleno).
    # Pista: usa st.success() y st.info().

    # Escribe aquí tu condicional if/else
    if prediccion:
        st.success("El jugador es una estrella")
    else:
        st.info("El jugador es uno del montón")
