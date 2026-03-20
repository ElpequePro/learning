import torch
import torch.nn as nn

# 1. Datos: 5km -> 20 fatiga, 10km -> 40 fatiga, 15km -> 60 fatiga
X = torch.tensor([[5.0], [10.0], [15.0], [20.0]], dtype=torch.float32)
y = torch.tensor([[20.0], [40.0], [60.0], [80.0]], dtype=torch.float32)

# 2. Definir la Neurona (Capa Lineal)
# Pista: nn.Linear(entradas, salidas)
modelo = nn.Linear(1, 1)

# 3. El "Castigo" (Función de pérdida) y el "Entrenador" (Optimizado)
criterio = nn.MSELoss()  # Mide cuánto se equivoca
optimizado = torch.optim.SGD(modelo.parameters(), lr=0.001)  # Corrige los errores

# TU RETO: Haz un bucle de 100 épocas
for i in range(1001):
    # 0. ¡IMPORTANTE! Limpiamos los errores anteriores
    optimizado.zero_grad()

    # A) La neurona prediga
    y_pred = modelo(X)

    # B) Calcules el error
    loss = criterio(y_pred, y)

    # C) Corrijas
    loss.backward()  # Calcula cuánto se ha equivocado cada parte de la neurona
    optimizado.step()  # Ajusta la neurona para fallar menos la próxima vez

    # EXTRA: Mostrar el progreso para que lo entiendas
    if i % 100 == 0:
        print(f"Época {i}: El error es de {round(loss.item(),2)}")

# 4. PRUEBA FINAL: ¿Qué pasa si corro 12km?
test_km = torch.tensor([[12.0]])
prediccion_final = modelo(test_km)
print(f"---")
print(
    f"Para 12km, la neurona predice una fatiga de: {round(prediccion_final.item(),2)}"
)
