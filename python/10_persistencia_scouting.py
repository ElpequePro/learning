import joblib
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# --- PARTE A: ENTRENAMIENTO (Solo se hace una vez) ---
X = np.array([[20, 15], [18, 12], [25, 10], [2, 1], [5, 3], [1, 4]])
y = np.array([1, 1, 1, 0, 0, 0])

modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(X, y)

# TU TRABAJO: Guarda el modelo
# Pista: joblib.dump(modelo, 'modelo_scouting.pkl')
try:
    joblib.dump(modelo, "10_modelo_scouting.pkl")
    print("Modelo guardado con éxito.")
except Exception:
    print(Exception)

# --- PARTE B: EL OJEADOR REMOTO ---
# Imagina que este es un programa nuevo que no sabe nada de los datos anteriores
# TU TRABAJO: Carga el modelo y predice para un jugador de [15, 10]
# Pista: modelo_cargado = joblib.load('modelo_scouting.pkl')
modelo_cargado = joblib.load("10_modelo_scouting.pkl")
jugador = modelo_cargado.predict(np.array([[15, 10]]))[0]
print(f"El jugador es del grupo {jugador}")

# Entra a `python` y ejecutar el _script_