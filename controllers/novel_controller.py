# controllers/novel_controller.py
from scraper.novel_scraper import NovelScraper
from models.novel_model import NovelModel

class NovelController:
    """Controlador para manejar la lógica de las novelas."""
    
    def __init__(self,url_base):
        #self.url_base = url_base
        self.scraper = NovelScraper(url_base)
    
    def buscar_novela(self, termino_busqueda):
        """Busca novelas según el término de búsqueda."""
        return self.scraper.buscar_novela(termino_busqueda)