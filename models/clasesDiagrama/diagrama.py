
from models.clasesDiagrama.linkDiagrama import LinkDiagrama


class Diagrama:
    """Clase que mantiene los objetos y los links del diagrama,
       Es la clase que se va a mandar al frontend para que consuma
    """
    i = 12345

    def __init__(self, objetosDelDiagrama, linksDelDiagrama):
        self.objetosDelDiagrama= objetosDelDiagrama
        self.linksDelDiagrama= linksDelDiagrama

    def nuevoObjetoDelDiagrama(self, objetoDelDiagrama):
        self.objetosDelDiagrama.append(objetoDelDiagrama)

    def cargarLasPropiedades(self, sujeto, lelsDePropiedades):
        return ''


    def generarLinks(self,desdeExpresion, lelsCategoricos):
        for lel in lelsCategoricos:
            nuevoLink = LinkDiagrama(desdeExpresion, lel.expresion)
            self.linksDelDiagrama.append(nuevoLink)
        