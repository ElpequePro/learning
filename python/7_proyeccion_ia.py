import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Datos de entrenamiento (X: Partidos, y: Goles)
# Nota: X debe ser una matriz (columna), por eso usamos .reshape(-1, 1)
partidos = np.array([5, 10, 15, 20, 25, 30, 35, 40]).reshape(-1, 1)
goles = np.array([1, 2, 2, 4, 5, 5, 7, 8])

# 2. CREAR EL MODELO DE IA
modelo = LinearRegression()

# 3. ENTRENAR EL MODELO (Aprender la relación entre partidos y goles)
modelo.fit(partidos, goles)

# --- TU RETO ---

# A) Predice cuántos goles tendrá el jugador cuando llegue a los 50, 80 y 100 partidos.
# Pista: usa modelo.predict(np.array([[50]]))
predict_50 = modelo.predict(np.array([[50]]))
predict_80 = modelo.predict(np.array([[80]]))
predict_100 = modelo.predict(np.array([[100]]))

# B) Visualiza la "Línea de Progresión".
# Dibuja los puntos reales (plt.scatter) y la línea que ha calculado la IA (plt.plot).
plt.title('Predicción IA')
plt.xlabel('Partidos')
plt.ylabel('Goles')
plt.scatter(partidos, goles, color="gray")
plt_x = np.array([0, 100]).reshape(-1, 1)
plt_y = modelo.predict(plt_x)
plt.scatter(50, predict_50, color="blue")
plt.scatter(80, predict_80, color="blue")
plt.scatter(100, predict_100, color="blue")
plt.savefig('7_predict.png')
plt.show()

# C) Imprime una conclusión: "¿Es una progresión de crack o de jugador de rotación?"
print(f"La IA predice que a los 100 partidos se podría llegar a los {round(predict_100[0])} goles!")