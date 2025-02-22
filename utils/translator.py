from googletrans import Translator

class NovelTranslator:
    """Clase para manejar la traducción de texto."""
    
    def __init__(self):
        self.translator = Translator()
    def detectar_idioma(self, texto):
           
            try:
                if not texto or texto.strip() == "":
                    print("Advertencia: El texto está vacío. No se puede detectar el idioma.")
                    return None
                
                partes = self.dividir_texto(texto)
                translator = Translator()
                
                idiomas_detectados = [translator.detect(parte).lang for parte in partes if parte.strip()]
                
                idioma_principal = max(set(idiomas_detectados), key=idiomas_detectados.count)
                
                return idioma_principal
            except Exception as e:
                print(f"No se pudo detectar el idioma. Continuando con la traducción... Error: {str(e)}")
                return None   
    def traducir_texto(self, texto, idioma_destino):
        """Traduce un texto al idioma de destino."""
        try:
            if not texto:
                raise ValueError("No hay texto para traducir.")

            partes = self.dividir_texto(texto)
            traduccion_completa = ""
            
            for parte in partes:
                traduccion = self.translator.translate(parte, dest=idioma_destino)
                if traduccion and traduccion.text:
                    traduccion_completa += traduccion.text + "\n"
            
            if not traduccion_completa:
                raise ValueError("La traducción no devolvió un texto válido.")

            return traduccion_completa
        except Exception as e:
            print(f"Error al traducir el capítulo: {str(e)}")
            return ""
    
    def dividir_texto(self, texto, limite=5000):
        """Divide el texto en partes más pequeñas para la traducción."""
        partes = []
        while len(texto) > limite:
            corte = texto[:limite].rfind(".")
            if corte == -1:
                corte = limite
            partes.append(texto[:corte + 1])
            texto = texto[corte + 1:]
        partes.append(texto)
        return partes