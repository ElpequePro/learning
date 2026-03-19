import pandas as pd
import matplotlib.pyplot as plt

# Dataset (Copia el del ejercicio 3)
data = {
    "jugador": [
        "Pedri",
        "Gavi",
        "De Jong",
        "Gündogan",
        "Fermín",
        "Casadó",
        "Olmo",
        "Bellingham",
        "Wirtz",
        "Musiala",
    ],
    "minutos": [2100, 450, 1800, 2500, 800, 1200, 1500, 2200, 2400, 1900],
    "goles": [4, 1, 2, 5, 6, 1, 8, 12, 11, 10],
    "asistencias": [9, 1, 5, 8, 2, 3, 7, 6, 15, 8],
}
df = pd.DataFrame(data)

# 1. Filtra y crea las columnas goles_90 y asistencias_90
# (Aplica la misma lógica de los 90 minutos que ya dominas)
df["goles_90"] = df["goles"] / (df["minutos"] / 90)
df["asistencias_90"] = df["asistencias"] / (df["minutos"] / 90)

# 2. Crea el gráfico
plt.figure(figsize=(10, 6))
plt.scatter(df["goles_90"], df["asistencias_90"], color="blue")

# 3. EL RETO: Anotar los nombres
# Pista: plt.annotate(texto, (x, y)) dentro de un bucle que recorra el DataFrame.
# Puedes usar: for i, txt in enumerate(df['jugador']):
#                  plt.annotate(txt, (df['goles_90'].iat[i], df['asistencias_90'].iat[i]))
for i, txt in enumerate(df['jugador']):
    plt.annotate(txt, (df['goles_90'].iat[i], df['asistencias_90'].iat[i]))

plt.title("Mapa de Especialistas: Goleadores vs Asistentes (por 90 min)")
plt.xlabel("Goles por 90 min")
plt.ylabel("Asistencias por 90 min")
plt.grid(True, linestyle="--", alpha=0.6)
plt.savefig('4_scatter.png')
plt.show()
