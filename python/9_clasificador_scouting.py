from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Datos: [[Goles, Asistencias]]
X = np.array(
    [
        [20, 15],  # Perfiles Estrella (Clase 1)
        [18, 12],
        [25, 10],
        [2, 1],  # Perfiles Relleno (Clase 0)
        [5, 3],
        [1, 4],
    ]
)

# Etiquetas: 1 = Estrella, 0 = Relleno
y = np.array([1, 1, 1, 0, 0, 0])

# Creamos el clasificador (que mire a los 3 vecinos más cercanos)
modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# --- TU TRABAJO ---
# 1. Tenemos un ojeo de un chaval de 17 años que lleva [12 goles y 9 asistencias].
# ¿Qué dice la IA? ¿Es un proyecto de Estrella o de Relleno?
# Pista: nuevo_jugador = np.array([[12, 9]])
jugador_1 = np.array([[12, 9]])
jugador_1_predict = modelo.predict(jugador_1)
print(f"El chaval de 17 años pertenece al grupo {jugador_1_predict[0]}")

# 2. Prueba con un jugador de [3 goles y 2 asistencias].
jugador_2 = np.array([[3, 2]])
jugador_2_predict = modelo.predict(jugador_2)
print(f"El otro chaval pertenece al grupo {jugador_2_predict[0]}")