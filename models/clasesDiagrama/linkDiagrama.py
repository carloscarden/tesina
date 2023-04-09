

class LinkDiagrama:
    """Representa las conexiones que tienen los objetos del diagrama, 
    de dónde parte y a dónde llega"""
    i = 12345

    def __init__(self, desde, hasta):
        self.desde = desde
        self.hasta= hasta