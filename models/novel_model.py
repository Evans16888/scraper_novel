class NovelModel:
    """Modelo de datos para representar una novela."""
    
    def __init__(self, nombre, url_novela, ultimo_capitulo, url_capitulo):
        self.nombre = nombre
        self.url_novela = url_novela
        self.ultimo_capitulo = ultimo_capitulo
        self.url_capitulo = url_capitulo