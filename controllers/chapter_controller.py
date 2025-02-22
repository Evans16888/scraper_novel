# controllers/chapter_controller.py
from scraper.chapter_scraper import ChapterScraper
from utils.translator import NovelTranslator
from utils.pdf_generator import PDFGenerator

class ChapterController:
    """Controlador para manejar la lógica de los capítulos."""
    
    def __init__(self, url_base):
        self.url_base = url_base
        self.scraper = ChapterScraper()
        self.translator = NovelTranslator()
        self.pdf_generator = PDFGenerator()
    
    def procesar_capitulo(self, url, numero_capitulo, idioma_destino):
        """
        Descarga, traduce y guarda un capítulo en formato PDF.
        
        Parámetros:
            url (str): La URL del capítulo.
            numero_capitulo (int): El número del capítulo.
            idioma_destino (str): El idioma al que se traducirá el capítulo.
        """
        try:
            # 1. Descargar el contenido del capítulo
            
            contenido = self.scraper.descargar_capitulo(url)
            if not contenido:
                print(f"Error: No se pudo descargar el capítulo {numero_capitulo}.")
                return
            
            # 2. Traducir el contenido
            contenido_traducido = self.translator.traducir_texto(contenido, idioma_destino)
            if not contenido_traducido:
                print(f"Error: No se pudo traducir el capítulo {numero_capitulo}.")
                return
            
            primeras_10_palabras = " ".join(contenido_traducido.split()[:10])  # Divide por espacios y toma las primeras 10
            print(f"Primeras 10 palabras: {primeras_10_palabras}")
            # 3. Guardar el contenido en un PDF
            nombre_archivo = f"capitulo_{numero_capitulo}.pdf"
            self.pdf_generator.guardar_en_pdf(contenido_traducido, nombre_archivo)
            print(f"Capítulo {numero_capitulo} guardado como {nombre_archivo}.")
        
        except Exception as e:
            print(f"Error al procesar el capítulo {numero_capitulo}: {str(e)}")
            
    def descargar_novela(self, url_novela, url_base, idioma_destino, modo_descarga, capitulo_inicio=None, capitulo_fin=None, capitulo_especifico=None):
            """
            Descarga una novela completa según los parámetros proporcionados.
            
            Parámetros:
                url_novela (str): La URL de la novela.
                url_base (str): La URL base del sitio web.
                idioma_destino (str): El idioma al que se traducirán los capítulos.
                modo_descarga (str): El modo de descarga ("todos", "rango", "especifico").
                capitulo_inicio (int): El número del primer capítulo a descargar (solo para modo "rango").
                capitulo_fin (int): El número del último capítulo a descargar (solo para modo "rango").
                capitulo_especifico (int): El número del capítulo específico a descargar (solo para modo "especifico").
            """
            try:
                # Obtener las URLs de los capítulos
                urls_capitulos = self.scraper.obtener_urls_capitulos(url_novela, url_base)
                if not urls_capitulos:
                    print("Error: No se encontraron capítulos para descargar.")
                    return
                
                # Determinar los capítulos a descargar según el modo
                if modo_descarga == "todos":
                    capitulos_a_descargar = range(1, len(urls_capitulos) + 1)
                elif modo_descarga == "rango":
                    if not capitulo_inicio or not capitulo_fin:
                        print("Error: Debes proporcionar un rango de capítulos.")
                        return
                    capitulos_a_descargar = range(capitulo_inicio, capitulo_fin + 1)
                elif modo_descarga == "especifico":
                    if not capitulo_especifico:
                        print("Error: Debes proporcionar un número de capítulo específico.")
                        return
                    capitulos_a_descargar = [capitulo_especifico]
                else:
                    print("Error: Modo de descarga no válido.")
                    return
                
                # Descargar y procesar cada capítulo
                for numero_capitulo in capitulos_a_descargar:
                    if 1 <= numero_capitulo <= len(urls_capitulos):
                        url = urls_capitulos[numero_capitulo - 1]
                        self.procesar_capitulo(url, numero_capitulo, idioma_destino)
                    else:
                        print(f"Advertencia: El capítulo {numero_capitulo} está fuera de rango.")
            
            except Exception as e:
                print(f"Error al descargar la novela: {str(e)}")