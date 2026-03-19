import numpy as np
from sklearn.linear_model import LinearRegression

# X: [Partidos, Remates a puerta]
X = np.array([
    [1, 1], [1, 3], [2, 5], [2, 2], [3, 8], [3, 4]
])
# y: Goles
y = np.array([0, 1, 1, 0, 2, 1])

modelo = LinearRegression()
modelo.fit(X, y)

# --- TU TRABAJO ---
# 1. Predice los goles para un jugador que juega 1 partido pero tira 10 VECES a puerta.
# Pista: modelo.predict(np.array([[1, 10]]))
predict_10_tiros = modelo.predict(np.array([[1, 10]]))

# 2. Imprime la conclusión: ¿Qué influye más en el gol, jugar muchos partidos o tirar mucho?
print(f"Si juegas 1 partido con 10 tiros a puerta, podrías tener un {round(predict_10_tiros[0], 2)} xG")