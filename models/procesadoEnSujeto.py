
from typing import List
from models.Lel import Lel


class ProcesadoEnSujeto:
    """ Acá se guarda todo lo que se puede procesar de un sujeto"""
    i = 12345

    def __init__(self, lelsDePropiedad: List[Lel], lelsDeNivel: List[Lel]):
        self.lelsDePropiedad=lelsDePropiedad 
        self.lelsDeNivel=  lelsDeNivel

    def nuevoLelDePropiedad(self, unLelDePropiedad: Lel):
        self.lelsDePropiedad.append(unLelDePropiedad)

    def nuevoLelDeNivel(self, unLelDeNivel: Lel):
        self.lelsDeNivel.append(unLelDeNivel)