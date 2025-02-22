# Importaciones de las pruebas
from .test_gui import TestMainWindow
from .test_scraper import TestNovelScraper
from .test_utils import TestTranslator
from .test_models import TestNovelModel

# Exportar las clases de pruebas
__all__ = ["TestMainWindow", "TestNovelScraper", "TestTranslator", "TestNovelModel"]