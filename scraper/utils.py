# scraper/utils.py
def obtener_encabezados():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
       
    }

def validar_url(url):
    return url.startswith("http://") or url.startswith("https://")

def extraer_dominio(url):
    from urllib.parse import urlparse
    parsed_url = urlparse(url)
    return parsed_url.netloc