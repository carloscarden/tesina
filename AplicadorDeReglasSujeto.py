from typing import List
from ReglasEnSujeto import ReglasEnSujeto
from models.Lel import Lel

from models.clasesDiagrama.DiagramasEnSujeto import DiagramasEnSujeto
from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.linkDiagrama import LinkDiagrama


class AplicadorDeReglasSujeto():

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
                    link = None
                    if(self.reglas.esArcoMultiple(encontradoEnSujeto, nivel.simbolo)):
                        # apply Rule 6 to o and o′, possibly change the arc from l to l′to multiple
                        link = LinkDiagrama.nuevoLinkMultiple( sujeto.simbolo, nivel.simbolo)
                    elif (self.reglas.esArcoOpcional(sujeto.datosParaProceso.docNotion, nivel.simbolo)):
                        # apply Rule 7 to o and o′, possibly change the arc from l to l′to optional
                        link= LinkDiagrama.nuevoLinkOpcional( sujeto.simbolo, nivel.simbolo)
                    else:
                        link= LinkDiagrama.nuevoHecho( sujeto.simbolo, nivel.simbolo)
                    self.diagramasEnSujeto.nuevoLinkDelDiagrama(link)

                    pass

                hayMasLels.extend(procesadoEnSujeto.lelsDeNivelNoProcesados)
                self.diagramasEnSujeto.nuevasPropiedades(procesadoEnSujeto.lelsDePropiedad)
                self.diagramasEnSujeto.nuevosNiveles(procesadoEnSujeto.lelsDeNivelNoProcesados)

            if not hayMasLels:
                break
            else:
                lelsAprocesar = hayMasLels



