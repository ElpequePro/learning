import pandas as pd

# 1. Dataset purgado y técnico (Modelos de Ámsterdam y Barcelona)
data = {
    "jugador": [
        "Messi",
        "Pedri",
        "Gavi",
        "Lamine Yamal",
        "Frenkie de Jong",
        "Dani Olmo",
        "Musiala",
    ],
    "equipo": [
        "Inter Miami",
        "FC Barcelona",
        "FC Barcelona",
        "FC Barcelona",
        "FC Barcelona",
        "FC Barcelona",
        "Bayern",
    ],
    "goles": [12, 4, 2, 7, 3, 6, 11],
    "asistencias": [8, 9, 5, 12, 6, 8, 10],
    "edad": [38, 21, 19, 17, 27, 26, 21],
}

# 2. Creamos el DataFrame
df = pd.DataFrame(data)

# --- TU NUEVO RETO (Sin rastro del Vardrid) ---
# A) Muestra solo los jugadores con una visión de juego radical (más de 7 asistencias).
print(df[df["asistencias"] > 7])

# B) Filtra y muestra solo a los integrantes del 'FC Barcelona'.
print(df[df["equipo"] == "FC Barcelona"])

# C) Calcula la media de edad de esta "cantera" de talentos.
print(f"Edad media: {df['edad'].median()}")

# D) ¿Quién es el jugador más joven del grupo? (Pista: usa .min() o .sort_values())
print(f"Jugador más joven: {df.loc[df['edad'] == df['edad'].min(), 'jugador'].iloc[0]}")

import matplotlib.pyplot as plt

# --- PARTE E: VISUALIZACIÓN ---

# Usamos el DataFrame 'df' que ya tienes creado
# Configuramos el gráfico: Barras agrupadas de Goles y Asistencias
df.plot(
    x="jugador", y=["goles", "asistencias"], kind="bar", color=["#004d98", "#a50044"]
)  # Colores Blaugrana

# Personalización del "estadio" (el gráfico)
plt.title("Comparativa de Productividad Ofensiva (Tiki-Taka Profile)")
plt.xlabel("Cerebros del equipo")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)  # Rotamos los nombres para que se lean bien
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Una rejilla sutil para medir mejor

# El toque final: Guardar o Mostrar
plt.tight_layout()  # Ajusta los márgenes automáticamente
plt.savefig('2_reporte.png')
plt.show()
