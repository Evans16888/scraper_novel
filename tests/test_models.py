import unittest
from models.novel_model import NovelModel
from models.chapter_model import ChapterModel

class TestNovelModel(unittest.TestCase):
    def test_novel_model_creation(self):
        """Prueba la creación de una instancia de NovelModel."""
        novela = NovelModel(
            nombre="Novela de Prueba",
            url_novela="https://www.novelhall.com/novela-de-prueba",
            ultimo_capitulo="Capítulo 100",
            url_capitulo="https://www.novelhall.com/capitulo-100"
        )
        self.assertEqual(novela.nombre, "Novela de Prueba")
        self.assertEqual(novela.url_novela, "https://www.novelhall.com/novela-de-prueba")
        self.assertEqual(novela.ultimo_capitulo, "Capítulo 100")
        self.assertEqual(novela.url_capitulo, "https://www.novelhall.com/capitulo-100")


class TestChapterModel(unittest.TestCase):
    def test_chapter_model_creation(self):
        """Prueba la creación de una instancia de ChapterModel."""
        capitulo = ChapterModel(
            numero=1,
            contenido="Este es el contenido del capítulo 1.",
            idioma="es"
        )
        self.assertEqual(capitulo.numero, 1)
        self.assertEqual(capitulo.contenido, "Este es el contenido del capítulo 1.")
        self.assertEqual(capitulo.idioma, "es")


if __name__ == "__main__":
    unittest.main()