import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

urls = [
    "https://www.transfermarkt.com/pedri/profil/spieler/683840",
    "https://www.transfermarkt.com/gavi/profil/spieler/646740",
    "https://www.transfermarkt.com/jamal-musiala/profil/spieler/580195",
    "https://url-que-no-existe.com/error" # URL falsa para probar el blindaje
]

headers = {"User-Agent": "Mozilla/5.0"}
lista_jugadores = []

for url in urls:
    try:
        res = requests.get(url, headers=headers, timeout=5)
        res.raise_for_status() # Lanza error si la web no responde bien
        soup = BeautifulSoup(res.text, "html.parser")
        
        # Extracción segura
        name = soup.select_one('.data-header__headline-wrapper').text.strip().split('\n')[-1].strip()
        
        # Buscamos el valor de mercado actual (el que está en grande)
        value_element = soup.select_one('.data-header__market-value-wrapper')
        if value_element:
            value_text = value_element.get_text()
            # Buscamos el número (ej: 80.00)
            match = re.search(r'(\d+[\.\,]?\d*)', value_text)
            value = float(match.group(1)) if match else 0.0
        else:
            value = 0.0
            
        lista_jugadores.append({"nombre": name, "valor": value})
        print(f"✅ Procesado: {name}")

    except Exception as e:
        print(f"❌ Error en {url}: {e}")

# Al salir del bucle, el programa sigue vivo aunque haya habido errores
df = pd.DataFrame(lista_jugadores)
print("\n--- INFORME FINAL ---")
print(df)