from typing import List
from ReglasEnSujeto import ReglasEnSujeto
from models.Lel import Lel

from models.clasesDiagrama.DiagramasEnSujeto import DiagramasEnSujeto
from models.clasesDiagrama.diagrama import Diagrama


class AplicadorDeReglasVerbo():

    def __init__(self, unDiagrama: Diagrama) -> None:
        self.diagramasEnSujeto = DiagramasEnSujeto(unDiagrama)
        self.reglas = ReglasEnSujeto()


    def aplicarReglasDeSujeto(self, lelsCategoricosDeVerbo: List[Lel], lels: List[Lel]):
        lelsAprocesar = lelsCategoricosDeVerbo

        while 1:
            hayMasLels = []

            for sujeto in  lelsAprocesar:

                # Encontrar todos los Categorical objects and subjects del verbo
                encontradoEnSujeto  = self.reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)

                #apply Rule 4 to o, get set Cl of levels, add them to l as children levels
                #apply Rule 5 to o, get set Pl of properties, add them to l as children levels
                procesadoEnSujeto = self.reglas.procesarElSujeto(encontradoEnSujeto, lels)

                niveles = procesadoEnSujeto.lelsDeNivel

                for nivel in niveles:
                    # apply Rule 6 to o and o′, possibly change the arc from l to l′to multiple
                    # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                    pass

                hayMasLels.extend(procesadoEnSujeto.lelsDeNivel)


            if not hayMasLels:
                break
            else:
                lelsAprocesar = hayMasLels





