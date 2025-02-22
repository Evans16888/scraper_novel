import os
from fpdf import FPDF
# utils/pdf_generator.py
from utils.file_utils import crear_directorio

class PDFGenerator:
    """Clase para generar archivos PDF."""

    def __init__(self):
        pass  # No es necesario inicializar self.pdf aquí

    def guardar_en_pdf(self, contenido, nombre_archivo):
        """
        Guarda el contenido en un archivo PDF.

        Parámetros:
            contenido (str): El contenido a guardar en el PDF.
            nombre_archivo (str): El nombre del archivo PDF.
        """
        try:
            self.pdf = FPDF()  # Se crea el objeto FPDF aquí
            # Crear la carpeta 'pdfs' si no existe
            crear_directorio("pdfs")

            # Configurar el PDF
            self.pdf.set_auto_page_break(auto=True, margin=15)
            self.pdf.add_page()

            # Obtener la ruta absoluta al archivo de fuente
            ruta_fuente = os.path.join(os.path.dirname(__file__), "fonts", "DejaVuSans.ttf")
            self.pdf.add_font("DejaVuSans", "", ruta_fuente, uni=True)
            self.pdf.set_font("DejaVuSans", size=12)

            # Agregar el contenido al PDF
            self.pdf.multi_cell(190, 10, contenido.encode('utf-8').decode('utf-8'))

            # Guardar el PDF en la carpeta 'pdfs'
            ruta_pdf = f"pdfs/{nombre_archivo}"
            self.pdf.output(ruta_pdf)
            print(f"PDF guardado como {ruta_pdf}")

        except (IOError, FileNotFoundError) as e:  # Manejo de excepciones más específico
            print(f"Error al guardar el PDF (problema de E/S o archivo no encontrado): {str(e)}")
        except Exception as e:
            print(f"Error al guardar el PDF: {str(e)}")
        finally:
            if hasattr(self, 'pdf') and self.pdf:  # Asegurarse de que self.pdf existe
                self.pdf.close()  # Cerrar el archivo PDF en el bloque finally
                print("Archivo PDF cerrado.")