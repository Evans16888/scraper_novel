import requests
import cloudscraper
from bs4 import BeautifulSoup
from .utils import obtener_encabezados, validar_url, extraer_dominio

class ChapterScraper:
    """Clase para manejar el scraping de capítulos."""

    def __init__(self):
        
        self.headers = obtener_encabezados()  # Usar encabezados personalizados
        self.scraper = cloudscraper.create_scraper()

    def obtener_urls_capitulos(self, url_novela, url_base):

        
        """Obtiene las URLs de los capítulos de una novela."""
        try:
               
            self.url_base=url_base
            if not validar_url(url_novela):
                raise ValueError(f"URL de la novela no válida: {url_novela}")

            response = self.scraper.get(url_novela, headers=self.headers, timeout=10)
            if response.status_code != 200:
                raise requests.exceptions.RequestException(f"Error de solicitud: {response.status_code}")

            soup = BeautifulSoup(response.text, 'html.parser')
            urls_capitulos = []

            if "novelhall.com" in self.url_base:
                morelist_div = soup.find('div', id='morelist')
                if morelist_div:
                    capitulos = morelist_div.find_all('li', class_='post-11')
                    for li in capitulos:
                        a_tag = li.find('a')
                        if a_tag and 'href' in a_tag.attrs:
                            href = a_tag['href']
                            url_completa = f"{self.url_base}{href}"
                            urls_capitulos.append(url_completa)
            elif "webnovel.com" in url_base:
                print("No es una URL de NovelHall.")
                pass
            elif "skynovels.net" in self.url_base:
            # Implementar lógica para skynovels.net
                pass
            
            elif "panchotranslations.com" in self.url_base:
            # Implementar lógica para skynovels.net
                pass
            
            elif "wuxiaworld.site" in self.url_base:
            # Implementar lógica para skynovels.net
                pass
            
            elif "www.wuxiaworld.comt" in self.url_base:
            # Implementar lógica para skynovels.net
                pass
            
            elif "novelasligeras.net" in self.url_base:
            # Implementar lógica para skynovels.net
                pass
            if not urls_capitulos:
                raise ValueError("No se encontraron capítulos en la página.")

            return urls_capitulos
        except Exception as e:
            print(f"Error al obtener las URLs de los capítulos: {str(e)}")
            return []
        
    def descargar_capitulo(self, url):
        
        """Descarga el contenido de un capítulo."""
        try:
            print(f"prueva de  {url} .")
            response = self.scraper.get(url, headers=self.headers, timeout=10)
            if response.status_code != 200:
                raise requests.exceptions.RequestException(f"Error de solicitud: {response.status_code}")
            
            soup = BeautifulSoup(response.text, 'html.parser')
            clases_contenido = ['chr-c', 'chapter-content', 'entry-content', 'epcontent entry-content', 'cha-content']
            
            contenido = None
            for clase in clases_contenido:
                elemento = soup.find(class_=clase)
                if elemento:
                    for br in elemento.find_all("br"):
                        br.replace_with("\n")
                    contenido = elemento.get_text(strip=True, separator="\n")
                    break
            
            if not contenido:
                raise ValueError("No se encontró contenido válido en la página.")
            
            return contenido
        except Exception as e:
            print(f"Error al descargar el capítulo: {str(e)}")
            return None    