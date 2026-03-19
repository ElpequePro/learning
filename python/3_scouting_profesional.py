import pandas as pd

# Simulamos el dataset de mediocentros
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

# --- RETO DE INGENIERÍA DE DATOS ---

# 1. LIMPIEZA: Filtra el DataFrame.
# Solo queremos jugadores con una muestra de minutos representativa (más de 500).
# Pista: Reasigna el df filtrando la columna 'minutos'.
df = df[df["minutos"] > 500]

# 2. MÉTRICA DE IMPACTO (KPI): Crea la columna 'impacto_90'.
# Queremos saber cuántos goles y asistencias genera un jugador CADA 90 MINUTOS.
# Fórmula lógica: (Suma de G+A) dividido entre (Minutos totales / 90).
# Pista: En Pandas, puedes operar con columnas como si fueran variables: df['A'] = df['B'] / df['C']
df["impacto_90"] = (df["goles"] + df["asistencias"]) / (df["minutos"] / 90)

# 3. RANKING: Ordena el DataFrame.
# Queremos ver arriba de la tabla a los que tienen mayor impacto_90.
# Pista: Busca el método '.sort_values()'. Cuidado con el parámetro 'ascending'.
df = df.sort_values(by='impacto_90',ascending=False)

# 4. RESULTADO: Imprime el Top 3.
# Pista: Usa el método '.head()'.
print(df.head(3))
