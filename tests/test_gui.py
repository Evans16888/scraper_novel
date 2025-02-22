import unittest
from tkinter import Tk
from gui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        """Configura el entorno para las pruebas."""
        self.root = Tk()
        self.app = MainWindow(self.root)

    def tearDown(self):
        """Limpia el entorno después de las pruebas."""
        self.root.destroy()

    def test_main_window_creation(self):
        """Prueba que la ventana principal se crea correctamente."""
        self.assertIsNotNone(self.app)
        self.assertEqual(self.app.root.title(), "Novel Downloader")

    def test_buscar_novela_interfaz(self):
        """Prueba la función de búsqueda de novelas en la interfaz."""
        # Simula la entrada de un término de búsqueda
        self.app.entry_busqueda.insert(0, "martial")
        self.app.buscar_novela_interfaz()

        # Verifica que se haya actualizado el Treeview
        resultados = self.app.tree.get_children()
        self.assertGreater(len(resultados), 0)


if __name__ == "__main__":
    unittest.main()