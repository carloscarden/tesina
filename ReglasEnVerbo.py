
import spacy


from spacy.language import Language
from spacy.tokens import Token
from spacy.tokens import Doc
from spacy.tokens import Span

from nltk.corpus import wordnet


from models.Lel import Lel
from models.encontradoEnSujeto import EncontradoEnSujeto
from models.procesadoEnSujeto import ProcesadoEnSujeto
from models.procesadoEnVerbo import ProcesadoEnVerbo
from models.Categoria import Categoria


from Reglas import Reglas
from typing import List



nlp = spacy.load("en_core_web_sm")


class ReglasEnVerbo(Reglas):

    def recuperarLosVerbos(self, lels: List[Lel]) -> List[Lel]:
          return [objeto for objeto in lels if objeto.categoria == Categoria.VERBO]
    
    
    def encontrarObjetosYsujetosDeVerbo(self, verbo: Lel):
        notionVerboDoc = verbo.devolverDocNotion(nlp)
        # procesar notion para que me de los objetos y sujetos
        lista_simboloes = self.procesarNotion(notionVerboDoc)
        return lista_simboloes



    def procesarElVerbo(self, sujetosYObjetosDeVerbo: List[str], lelMockeado: List[Lel])-> ProcesadoEnVerbo:
        procesadoEnVerbo = ProcesadoEnVerbo([],[])
        for simbolo in sujetosYObjetosDeVerbo :
            # Encontrar el LEL correspondiente
            lelDeVerboAprocesar = list( filter( lambda obj_lel: self.esLelBuscado(obj_lel, simbolo) , 
                                           lelMockeado))
            if lelDeVerboAprocesar:
                doc = lelDeVerboAprocesar[0].devolverDocNotion(nlp)
                medidas = [tok.text for tok in doc if self.es_medida(tok.text)]
                if(len(medidas)>0):

                        # REGLA 2

                    # Numerical objects and subjects of verbs give origin to measures.
                    # buscar entre los objetos y sujetos del notion un objeto numerico
                    procesadoEnVerbo.nuevoLelDeMedida(lelDeVerboAprocesar[0])
                    
                else:
                        # REGLA 3
                    # Categorical objects and subjects of verbs give origin to dimensions
                    # Si no cae en la categoria de medida, entonces es un categorico del verbo
                    procesadoEnVerbo.nuevoLelCategoricoDeVerbo(lelDeVerboAprocesar[0])
                
                # Actualizo el docNotion del lel
                lelDeVerboAprocesar[0].datosParaProceso.docNotion = doc        
        return procesadoEnVerbo


