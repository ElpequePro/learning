import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re # Para buscar patrones

# 1. Lista de objetivos
urls = [
    "https://www.transfermarkt.com/pedri/profil/spieler/683840",
    "https://www.transfermarkt.com/gavi/profil/spieler/646740",
    "https://www.transfermarkt.com/jamal-musiala/profil/spieler/580195"
]

headers = {"User-Agent": "Mozilla/5.0"}
lista_jugadores = []

# 2. Bucle de Scraping
for url in urls:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    
    # --- TU TRABAJO AQUÍ ---
    # Extrae el nombre y el valor de mercado.
    # Pista: Reutiliza la lógica de '1_scraping.py' pero dentro del bucle.
    name = soup.select('.data-header .data-header__headline-wrapper strong')[0].text.strip()
    value_raw = soup.select('.data-header__box--small')[0].text # €150.00m Last update: 16/03/2026
    value = float(re.search(r'(\d+\.\d+)', value_raw).group(1)) # 150.00
    
    # Al final de cada iteración, guarda los datos en un diccionario:
    # lista_jugadores.append({"nombre": nombre, "valor": valor})
    lista_jugadores.append({"nombre": name, "valor": value})

# 3. Procesamiento con Pandas
df = pd.DataFrame(lista_jugadores)

# 4. Visualización
# Haz el gráfico de barras del valor de mercado.
plt.title('Valor de Mercado')
plt.ylabel('Precio (millones)')
plt.xlabel('Jugador')
plt.bar(df['nombre'], df['valor'])
plt.savefig('5_scraping.png')
plt.show()