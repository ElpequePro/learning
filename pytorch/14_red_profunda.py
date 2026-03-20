import torch
import torch.nn as nn

# 1. DATOS COMPLEJOS (X: [Edad, Goles] -> y: Valor en Millones)
# Jugadores: [20años, 15goles], [32años, 15goles], [22años, 5goles], [35años, 2goles]
X = torch.tensor(
    [[20.0, 15.0], [32.0, 15.0], [22.0, 5.0], [35.0, 2.0]], dtype=torch.float32
)
y = torch.tensor([[80.0], [40.0], [30.0], [5.0]], dtype=torch.float32)


# 2. DEFINICIÓN DE LA RED (EL CEREBRO)
class RedScouting(nn.Module):
    def __init__(self):
        super().__init__()
        # TU RETO: Define la estructura.
        # Capa 1: Entrada de 2 datos (Edad/Goles) -> 10 neuronas ocultas.
        self.capa1 = nn.Linear(2, 10)

        # Filtro de activación (ReLU): Ignora datos inútiles.
        self.relu = nn.ReLU()

        # Capa 2: Las 10 neuronas anteriores -> 1 resultado final (Precio).
        self.capa2 = nn.Linear(10, 1)

    def forward(self, x):
        # TU RETO: Conecta las piezas en orden.
        # Pasa 'x' por capa1, luego por relu, y el resultado por capa2.
        x = self.capa1(x)
        x = self.relu(x)
        x = self.capa2(x)
        return x


# Instanciamos el modelo
modelo = RedScouting()

# 3. CONFIGURACIÓN
# TU RETO: Elige un optimizador y una función de error.
# Pista: Usa lo que aprendiste en el Ejercicio 13 (MSELoss y SGD).
criterio = nn.MSELoss()
# ¡Ojo! El learning rate (lr) debe ser muy bajo para no explotar.
optimizado = torch.optim.SGD(modelo.parameters(), lr=0.0001)

# 4. BUCLE DE ENTRENAMIENTO
# TU RETO: Entrena durante 2000 épocas.
# Pista: No olvides el .zero_grad(), .backward() y .step().
for i in range(2001):
    # Escribe aquí el proceso de entrenamiento
    optimizado.zero_grad()

    y_pred = modelo(X)
    loss = criterio(y_pred, y)

    loss.backward()
    optimizado.step()

    if i % 200 == 0:
        # Pista: usa loss.item() para imprimir el error
        print(f"Época {i}: Error = {round(loss.item(), 2)}")

# 5. TEST FINAL
# TU RETO: Predice el valor de un jugador de 25 años con 12 goles.
test_jugador = torch.tensor([[25.0, 12.0]])
# Pista: pasa el test_jugador por el modelo
resultado = modelo(test_jugador)
print(f"---")
print(f"Valor estimado para el jugador: {round(resultado.item(), 2)} M€")
