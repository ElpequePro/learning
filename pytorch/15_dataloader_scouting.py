import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# 1. GENERACIÓN DE DATOS (1000 jugadores simulados)
X = torch.randn(1000, 2) 
y = torch.randint(0, 3, (1000,)) 

# 2. EL CONTENEDOR DE DATOS
# TU RETO: Crea el Dataset y el DataLoader.
# Pista: Dataset empaqueta X e y. DataLoader los divide en grupos (batch_size=32).
dataset = TensorDataset(X, y)
train_loader = DataLoader(dataset, batch_size=32, shuffle=True)

# 3. LA RED MULTICLASE
class RedPosiciones(nn.Module):
    def __init__(self):
        super().__init__()
        # Usamos Sequential para agrupar Capa1 -> ReLU -> Capa2
        self.red = nn.Sequential(
            nn.Linear(2, 16),
            nn.ReLU(),
            nn.Linear(16, 3) # 3 salidas para: Defensa, Medio, Delantero
        )
    
    def forward(self, x):
        # TU RETO: Pasa 'x' por self.red y devuélvelo.
        x = self.red(x)
        return x

modelo = RedPosiciones()

# 4. CONFIGURACIÓN
# TU RETO: Usa CrossEntropyLoss y el optimizador Adam (lr=0.01).
criterio = nn.CrossEntropyLoss()
optimizado = torch.optim.Adam(modelo.parameters(), lr=0.01)

# 5. BUCLE DE ENTRENAMIENTO (Lógica de Batches)
print("Entrenando...")
for epoca in range(101):
    for batch_x, batch_y in train_loader:
        # TU RETO: Aplica los 4 pasos mágicos que usaste en el ejercicio 13 y 14.
        # 1. Limpiar gradientes
        # 2. Predicción (usando batch_x)
        # 3. Calcular error (usando batch_y)
        # 4. Backpropagation y paso del optimizador
        
        # ... escribe los 4 pasos aquí ...
        optimizado.zero_grad()
        pred = modelo(batch_x)
        loss = criterio(pred, batch_y)
        loss.backward()
        optimizado.step()

    if epoca % 10 == 0:
        print(f"Época {epoca} completada")

# 6. TEST
test_jugador = torch.tensor([[2.0, -1.0]])
prediccion = modelo(test_jugador)
# Pista: torch.argmax saca el índice del valor más alto.
posicion = torch.argmax(prediccion).item()
print(f"Resultado: {posicion}")