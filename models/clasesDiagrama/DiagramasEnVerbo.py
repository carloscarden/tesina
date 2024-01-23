from typing import List
from models.Lel import Lel
from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama
from models.procesadoEnVerbo import ProcesadoEnVerbo


class DiagramasEnVerbo:
    """Clase para construir los diagramas que apareceran en los verbos
    """
    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama=  unDiagrama

    def nuevoHecho(self, verbo: Lel):
        nuevoVerbo = ObjetoDiagrama.nuevoHecho(verbo.simbolo,  TipoObjetoDiagrama.HECHO)
        self.diagrama.nuevoObjetoDelDiagrama(nuevoVerbo)
    

    def generarObjetosDelDiagramaPorVerbo(self, procesadoEnVerbo: ProcesadoEnVerbo, simbolo: str):
        
        # all the elements in lelsDeMedida should be defined as 
        # measures of the fact corresponding to v
        self.nuevasMedidasDeVerbo(procesadoEnVerbo.lelsDeMedida, simbolo)
        
        
        # all the elements on lelsCategoricosDeVerbo  should be defined as 
        # dimensions of the fact corresponding to v
        self.nuevasDimensionesDeVerbo(procesadoEnVerbo.lelsCategoricosDeVerbo)


    def nuevasMedidasDeVerbo(self, lelsDeMedida: List[Lel], verboLel: str):
        for lel in lelsDeMedida:
            nuevaMedida = ObjetoDiagrama.nuevaMedida(lel.simbolo, verboLel)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)


    def nuevasDimensionesDeVerbo(self, lelsDeDimensiones: List[Lel], verboLel: List[Lel]):
        for lel in lelsDeDimensiones:
            nuevaMedida = ObjetoDiagrama.nuevaDimension(lel.simbolo, verboLel)
            self.diagrama.nuevoObjetoDelDiagrama(nuevaMedida)