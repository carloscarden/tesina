
from models.Lel import Lel
from typing import List


class ProcesadoEnVerbo:
    """Aca se guarda todo lo que se puede procesar en un verbo"""
    i = 12345

    def __init__(self, lelsDeMedida: List[Lel], lelsCategoricosDeVerbo: List[Lel]):
        self.lelsDeMedida=lelsDeMedida 
        self.lelsCategoricosDeVerbo=  lelsCategoricosDeVerbo

    def nuevoLelDeMedida(self, unLelDeMedida):
        self.lelsDeMedida.append(unLelDeMedida)

    def nuevoLelCategoricoDeVerbo(self, unLelCategoricoDeVerbo):
        self.lelsCategoricosDeVerbo.append(unLelCategoricoDeVerbo)

    def devolverLelsDeMedida(self):
        if(self.lelsDeMedida):
            return self.lelsDeMedida[0].expresion
        return ''