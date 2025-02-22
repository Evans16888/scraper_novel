import unittest
import os
from utils.translator import NovelTranslator
from utils.pdf_generator import PDFGenerator
from utils.file_utils import crear_directorio, limpiar_directorio, obtener_ruta_pdf

class TestTranslator(unittest.TestCase):
    def setUp(self):
        """Configura el traductor para las pruebas."""
        self.translator = NovelTranslator()

    def test_traducir_texto(self):
        """Prueba la traducción de texto."""
        texto_original = "Hello, world!"
        texto_traducido = self.translator.traducir_texto(texto_original, "es")
        self.assertIn("Hola", texto_traducido)

    def test_traducir_texto_vacio(self):
        """Prueba la traducción de texto vacío."""
        texto_traducido = self.translator.traducir_texto("", "es")
        self.assertEqual(texto_traducido, "")

    def test_dividir_texto(self):
        """Prueba la división de texto en partes más pequeñas."""
        texto_largo = "a" * 6000  # Texto de 6000 caracteres
        partes = self.translator.dividir_texto(texto_largo)
        self.assertGreater(len(partes), 1)
        for parte in partes:
            self.assertLessEqual(len(parte), 5000)


class TestPDFGenerator(unittest.TestCase):
    def setUp(self):
        """Configura el generador de PDFs para las pruebas."""
        self.pdf_generator = PDFGenerator()

    def test_guardar_en_pdf(self):
        """Prueba la generación de un archivo PDF."""
        contenido = "Este es un contenido de prueba."
        nombre_archivo = "test.pdf"
        self.pdf_generator.guardar_en_pdf(contenido, nombre_archivo)
        self.assertTrue(os.path.exists(nombre_archivo))
        os.remove(nombre_archivo)  # Limpiar después de la prueba


class TestFileUtils(unittest.TestCase):
    def test_crear_directorio(self):
        """Prueba la creación de un directorio."""
        ruta = "test_dir"
        crear_directorio(ruta)
        self.assertTrue(os.path.exists(ruta))
        os.rmdir(ruta)  # Limpiar después de la prueba

    def test_limpiar_directorio(self):
        """Prueba la limpieza de un directorio."""
        ruta = "test_dir"
        crear_directorio(ruta)
        with open(os.path.join(ruta, "test.txt"), "w") as f:
            f.write("Prueba")
        limpiar_directorio(ruta)
        self.assertEqual(len(os.listdir(ruta)), 0)
        os.rmdir(ruta)  # Limpiar después de la prueba

    def test_obtener_ruta_pdf(self):
        """Prueba la obtención de la ruta de un archivo PDF."""
        ruta = obtener_ruta_pdf("test.pdf")
        self.assertTrue(ruta.startswith("pdfs/"))
        self.assertTrue(ruta.endswith("test.pdf"))


if __name__ == "__main__":
    unittest.main()