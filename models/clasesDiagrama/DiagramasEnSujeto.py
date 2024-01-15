from typing import List
from models.Lel import Lel
from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.linkDiagrama import LinkDiagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama


class DiagramasEnSujeto:
    """Clase para construir los diagramas que apareceran en los sujetos
    """
    i = 12345

    def __init__(self, unDiagrama: Diagrama):
        self.diagrama = unDiagrama


    def nuevosNiveles(self,  lelsDeNivel, sujeto ):
        return ''    
    

    def nuevasPropiedades(self,  lelsDeNivel, sujeto ):
        return ''    
    

    def nuevosArcosMultiples(self,  lelsDeNivel, sujeto ):
        return ''    


    def nuevosArcosOpcionales(self,  lelsDeNivel, sujeto ):
        return ''    