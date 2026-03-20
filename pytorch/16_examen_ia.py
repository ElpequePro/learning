import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

# 1. DATASET PROFESIONAL
# [Goles, Asistencias, Recuperaciones, Pases]
X = torch.tensor(
    [
        [0.1, 0.1, 9.5, 50.0],  # Defensa 1
        [0.2, 0.0, 8.0, 40.0],  # Defensa 2
        [0.5, 0.8, 4.0, 70.0],  # Medio 1
        [0.4, 0.9, 5.0, 65.0],  # Medio 2
        [1.2, 0.3, 1.0, 20.0],  # Delantero 1
        [0.9, 0.2, 2.0, 25.0],  # Delantero 2
    ],
    dtype=torch.float32,
)

y = torch.tensor([0, 0, 1, 1, 2, 2], dtype=torch.long)

# TU RETO: Crea el DataLoader aquí
dataset = TensorDataset(X, y)
loader = DataLoader(dataset, shuffle=True, batch_size=32)


# 2. MODELO DE EXAMEN
class RedExamen(nn.Module):
    # TU RETO: Define las 3 capas lineales y las 2 activaciones ReLU
    def __init__(self):
        super().__init__()

        # Entran 4 campos [Goles, Asistencias, Recuperaciones, Pases]
        self.capa1 = nn.Linear(4, 16)
        self.capa2 = nn.Linear(16, 8)
        # Salen 3 campos [Muro, Motor, Finalizador]
        self.capa3 = nn.Linear(8, 3)

        self.relu1 = nn.ReLU()
        self.relu2 = nn.ReLU()

    def forward(self, x):
        # TU RETO: Conecta la tubería
        x = self.capa1(x)
        x = self.relu1(x)
        x = self.capa2(x)
        x = self.relu2(x)
        x = self.capa3(x)
        return x


modelo = RedExamen()

# 3. ENTRENAMIENTO
# TU RETO: Configura el criterio, optimizador y el bucle de 500 épocas
criterio = nn.CrossEntropyLoss()
optimizador = torch.optim.Adam(modelo.parameters(), lr=0.01)

for i in range(501):
    for batch_x, batch_y in loader:
        optimizador.zero_grad()

        pred = modelo(batch_x)
        loss = criterio(pred, batch_y)

        loss.backward()
        optimizador.step()

        if i % 50 == 0:
            print(f"Ronda {i} completada")

# 4. EVALUACIÓN FINAL
# Predicción para: [0.1, 0.2, 8.5, 45.0]
jugador = torch.tensor([0.1, 0.2, 8.5, 45.0], dtype=torch.float32)
prediccion = modelo(jugador)
posicion = torch.argmax(prediccion).item()

if posicion == 0:
    posicion = "defensa"
elif posicion == 1:
    posicion = "medio"
elif posicion == 2:
    posicion = "delantero"

print(f"El jugador es {posicion}")
