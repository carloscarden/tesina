
from typing import List
from models.clasesDiagrama.linkDiagrama import LinkDiagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama


class Diagrama:
    """Clase que mantiene los objetos y los links del diagrama,
       Es la clase que se va a mandar al frontend para que consuma
    """
    i = 12345

    def __init__(self, objetosDelDiagrama: List[ObjetoDiagrama], linksDelDiagrama: List[LinkDiagrama]):
        self.objetosDelDiagrama= objetosDelDiagrama
        self.linksDelDiagrama= linksDelDiagrama

    def nuevoObjetoDelDiagrama(self, objetoDelDiagrama):
        self.objetosDelDiagrama.append(objetoDelDiagrama)



    def generarLinks(self,desdeExpresion, lelsCategoricos):
        for lel in lelsCategoricos:
            nuevoLink = LinkDiagrama(desdeExpresion, lel.expresion)
            self.linksDelDiagrama.append(nuevoLink)
        
    def cargarLosNiveles(self, sujeto, lelsDeNivel ):
        return ''    