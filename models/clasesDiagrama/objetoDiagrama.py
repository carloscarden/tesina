
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama


class ObjetoDiagrama:
    """Del diagrama representa toda la informacion para saber qué dibujar"""
    i = 12345

    def __init__(self, simbolo, aQuienPertenece, categoria):
        self.key = simbolo
        self.prop1= aQuienPertenece
        self.category= categoria
    
    @classmethod
    def nuevoHecho(self, simbolo):
        return ObjetoDiagrama(simbolo, '',  TipoObjetoDiagrama.HECHO)
    
    @classmethod
    def nuevaMedida(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece, TipoObjetoDiagrama.MEDIDA)

    @classmethod
    def nuevaDimension(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.DIMENSION)


    @classmethod
    def nuevoNivel(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.NIVEL)


    @classmethod
    def nuevaPropiedad(self, simbolo, aQuienPertenece):
        return ObjetoDiagrama(simbolo, aQuienPertenece,  TipoObjetoDiagrama.PROPIEDAD)
