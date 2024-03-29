from typing import List
from ReglasEnVerbo import ReglasEnVerbo
from models.Lel import Lel
from models.clasesDiagrama.DiagramasEnVerbo import DiagramasEnVerbo
from models.clasesDiagrama.diagrama import Diagrama


class AplicadorDeReglasVerbo():

    def __init__(self, diagrama: Diagrama):
        self.diagramasEnVerbo =DiagramasEnVerbo(diagrama) 
        self.reglasVerbo = ReglasEnVerbo()


    def aplicarReglasDeVerbo(self, lels: List[Lel]):

                # REGLA 1
        # Verbs give origin to facts. 
        verbos = self.reglasVerbo.recuperarLosVerbos(lels)
        
        for v in verbos:


            # v should be defined as a fact
            self.diagramasEnVerbo.nuevoHecho(v)

            # Encontrar todos los Categorical objects and subjects del verbo
            sujetosYObjetosDeVerbo = self.reglasVerbo.encontrarObjetosYsujetosDeVerbo(v.nocion)


            # apply Rule 2 to v, get set Mf of measures, add them to f
            # apply Rule 3 to v, get set Df of dimensions, add them to f
            procesadoEnVerbo = self.reglasVerbo.procesarElVerbo(sujetosYObjetosDeVerbo, lels)


            self.diagramasEnVerbo.generarObjetosDelDiagramaPorVerbo(procesadoEnVerbo, v.simbolo)

            v.terminadoDeProcesarVerbo()

        return procesadoEnVerbo.lelsCategoricosDeVerbo
    