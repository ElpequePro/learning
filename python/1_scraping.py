"""
🎯 RETO: OPERACIÓN PULGA (Scraping de TransferMarkt)

ENUNCIADO:
1. Utiliza la librería 'requests' para obtener el HTML de la página de Messi.
2. Utiliza 'BeautifulSoup' para navegar por el DOM.
3. Extrae y limpia los siguientes datos:
   - Nombre completo.
   - Edad actual.
   - Goles en la temporada actual.
   - Asistencias en la temporada actual.

PISTAS PARA NAVEGAR EL DOM:
- El nombre suele estar en un <h1> o una clase que contenga 'main-header'.
- La edad está dentro de la lista de 'datos principales'.
- Los goles están en una tabla; busca el <td> que corresponde a la estadística de goles.
"""

import requests
from bs4 import BeautifulSoup

# URL de la ficha de Messi
url = "https://www.transfermarkt.com/lionel-messi/profil/spieler/28003"

# Cabecera necesaria para que TransferMarkt no nos bloquee (Simula un navegador)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# --- TU CÓDIGO EMPIEZA AQUÍ ---

# 1. Haz la petición (requests.get...)
res = requests.get(url=url, headers=headers)
data = res.text

# 2. Crea el objeto BeautifulSoup para manejar el DOM
soup = BeautifulSoup(data, "html.parser")

# 3. Busca los elementos por clase o etiqueta y extrae el texto (.text)
name = soup.select(".info-table__content.info-table__content--bold")[0].text.strip()
age = soup.select(".info-table__content.info-table__content--bold a")[0].text.strip()
value = soup.select(".data-header__box--small")[0].text.strip()

# Buscamos la fila que tiene la clase de 'Total' (grid-row--dark suele ser la de totales)
total_row = soup.select_one(".grid-row--dark")

if total_row:
    # Dentro de esa fila, pillamos todas las celdas
    cells = total_row.select(".grid__cell--center")
    
    # Ahora asignamos por posición en esa fila específica
    matches = cells[0].text.strip()
    goals = cells[1].text.strip()
    assists = cells[2].text.strip()
else:
    matches, goals, assists = "0", "0", "0"

# 4. Imprime los resultados con un print()
print(f"Name: {name}\nAge: {age}\nMarket Value: {value}\nMLS: {matches}M {goals}G {assists}A")

# Nota: 'matches', 'goals' y 'assists' no las coge