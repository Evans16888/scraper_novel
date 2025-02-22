# Importaciones de los módulos de scraping
from .novel_scraper import NovelScraper
from .chapter_scraper import ChapterScraper
from .utils import obtener_encabezados

# Exportar las clases y funciones principales
__all__ = ["NovelScraper", "ChapterScraper", "obtener_encabezados"]