import requests
import cloudscraper
from bs4 import BeautifulSoup
# scraper/novel_scraper.py
from scraper.utils import obtener_encabezados, validar_url, extraer_dominio

class NovelScraper:
    """Clase para manejar el scraping de novelas."""

    def __init__(self, url_base):
        self.url_base = url_base
        self.headers = obtener_encabezados()  # Usar encabezados personalizados
        self.scraper = cloudscraper.create_scraper()

    def buscar_novela(self, termino_busqueda):
        """Busca novelas en la URL base."""
        try:
            print(f"mostrada la caca: {self.url_base}")  # ✅ Obtener el valor real de la URL
            
            if not validar_url(self.url_base):  # ✅ Pasar la cadena real a la función
                raise ValueError(f"URL base no válida: {self.url_base}")

            url_busqueda = f"{self.url_base}/index.php?s=so&module=book&keyword={termino_busqueda}"
            response = self.scraper.get(url_busqueda, headers=self.headers)
            if response.status_code != 200:
                raise Exception(f"Error al realizar la búsqueda: {response.status_code}")

            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='section3 inner mt30')
            if not section:
                raise Exception("No se encontró la sección de resultados.")

            filas = section.find('table').find('tbody').find_all('tr')
            if not filas:
                raise Exception("No se encontraron novelas en los resultados.")

            novelas = []
            for fila in filas:
                celda_novela = fila.find_all('td')[1]
                enlace_novela = celda_novela.find('a')
                if enlace_novela:
                    nombre_novela = enlace_novela.get_text(strip=True)
                    url_novela = f"{self.url_base}{enlace_novela['href']}"
                else:
                    continue

                celda_capitulo = fila.find_all('td')[2]
                enlace_capitulo = celda_capitulo.find('a')
                if enlace_capitulo:
                    ultimo_capitulo = enlace_capitulo.get_text(strip=True)
                    url_capitulo = f"{self.url_base}{enlace_capitulo['href']}"
                else:
                    ultimo_capitulo = "No disponible"
                    url_capitulo = ""

                novelas.append({
                    'nombre': nombre_novela,
                    'url_novela': url_novela,
                    'ultimo_capitulo': ultimo_capitulo,
                    'url_capitulo': url_capitulo
                })

            return novelas
        except Exception as e:
            print(f"Error en la búsqueda: {str(e)}")
            return None