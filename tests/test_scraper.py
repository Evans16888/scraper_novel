import unittest
from scraper.novel_scraper import NovelScraper
from scraper.chapter_scraper import ChapterScraper

class TestNovelScraper(unittest.TestCase):
    def setUp(self):
        """Configura el scraper para las pruebas."""
        self.scraper = NovelScraper("https://www.novelhall.com")

    def test_buscar_novela(self):
        """Prueba la búsqueda de novelas."""
        resultados = self.scraper.buscar_novela("martial")
        self.assertIsNotNone(resultados)
        self.assertGreater(len(resultados), 0)

        # Verifica que cada novela tenga los campos esperados
        for novela in resultados:
            self.assertIn("nombre", novela)
            self.assertIn("url_novela", novela)
            self.assertIn("ultimo_capitulo", novela)
            self.assertIn("url_capitulo", novela)


class TestChapterScraper(unittest.TestCase):
    def setUp(self):
        """Configura el scraper para las pruebas."""
        self.scraper = ChapterScraper("https://www.novelhall.com")

    def test_obtener_urls_capitulos(self):
        """Prueba la obtención de URLs de capítulos."""
        url_novela = "https://www.novelhall.com/novela-de-prueba"
        urls_capitulos = self.scraper.obtener_urls_capitulos(url_novela)
        self.assertIsNotNone(urls_capitulos)
        self.assertGreater(len(urls_capitulos), 0)

        # Verifica que las URLs sean válidas
        for url in urls_capitulos:
            self.assertTrue(url.startswith("https://"))


if __name__ == "__main__":
    unittest.main()