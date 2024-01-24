
import spacy


from spacy.language import Language
from spacy.tokens import Token
from spacy.tokens import Doc
from spacy.tokens import Span

from nltk.corpus import wordnet
from Reglas import Reglas


from models.Lel import Lel
from models.encontradoEnSujeto import EncontradoEnSujeto
from models.procesadoEnSujeto import ProcesadoEnSujeto

from typing import List



nlp = spacy.load("en_core_web_sm")


class ReglasEnSujeto(Reglas):


    def encontrarLosObjetosCategoricosDeSujetos(self, lelsCategoricos: Lel):
        doc = lelsCategoricos.devolverDocNotion(nlp)

        # Lista de palabras objetivo
        target_words = ["has", "belongs", "comprised", "covered", "incorporated", "involves", 
                    "according","according to", "characterized by","manufactured"]

        encontradoEnSujeto = EncontradoEnSujeto([],[], [])


        for token in doc:
            esCompuesta = self.fraseCompuesta(token, doc, target_words)
        
            if token.text in target_words or esCompuesta:
                # Encuentra el sujeto y el objeto de la relación
                obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]

                if(esCompuesta):
                    obj = [w for w in doc[token.i + 1].rights  if w.dep_ == "dobj" or w.dep_ == "pobj"]
                else:
                    obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]



                # Busca el objeto en la lista de sustantivos y adjetivos a la derecha
                if not obj:
                    if(esCompuesta):
                        obj = [w for w in doc[token.i + 1].rights if w.dep_ == "amod" or w.dep_ == "nsubj"]
                    else:
                        obj = [w for w in token.rights if w.dep_ == "amod" or w.dep_ == "nsubj"]
            
                # Maneja las preposiciones
                if not obj:
                    if(esCompuesta):
                        obj = [w for w in doc[token.i + 1].rights if w.dep_ == "prep"]
                    else:
                        obj = [w for w in token.rights if w.dep_ == "prep"]
                    if obj:
                        obj = [w for w in obj[0].rights if w.dep_ == "pobj"]
                if obj:
                    # Find noun chunks that contain the object
                    noun_chunk = next((nc for nc in doc.noun_chunks if nc.root == obj[0] ), None)
                    encontradoEnSujeto.nuevoObjeto(noun_chunk)
        return encontradoEnSujeto


    def procesarElSujeto(self, encontradoEnSujeto: EncontradoEnSujeto, lelMockeado) -> ProcesadoEnSujeto:

        procesadoEnSujeto = ProcesadoEnSujeto([],[])
        self.procesarLosObjectsSimples(procesadoEnSujeto, encontradoEnSujeto.objectsSimple, lelMockeado)
        self.procesarLosPalabraDoble(procesadoEnSujeto, encontradoEnSujeto.nounChunks, lelMockeado)

        return procesadoEnSujeto


    def procesarLosObjectsSimples(self, procesadoEnSujeto: ProcesadoEnSujeto, 
                                   objectsSimple, lelMockeado):
        
        for simbolo in objectsSimple:
            aBuscar = simbolo.text.lower()

            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscado(lel, aBuscar) , 
                                           lelMockeado))
            self.tipoDeLelQueEsElSujeto(lelDeSujetoAprocesar, procesadoEnSujeto)                               


    def procesarLosPalabraDoble(self, procesadoEnSujeto, nounChunks, lelMockeado):
        for nc in nounChunks:
            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscadoCompuesto(lel, nc) , 
                                           lelMockeado))
            self.tipoDeLelQueEsElSujeto(lelDeSujetoAprocesar, procesadoEnSujeto)                               


    def tipoDeLelQueEsElSujeto(self, lelDeSujetoAprocesar:List[Lel], procesadoEnSujeto: ProcesadoEnSujeto):
        if lelDeSujetoAprocesar :
            doc = lelDeSujetoAprocesar[0].devolverDocNotion(nlp)
            medidas = [tok.text for tok in doc if self.es_medida(tok.text)]
            if(len(medidas)>0):
                     #Rule 5. 
                # Numerical objects and subjects of objects or subjects give origin to properties.
                # buscar entre los objetos y sujetos del notion un objeto numerico
                procesadoEnSujeto.nuevoLelDePropiedad(lelDeSujetoAprocesar[0])
                lelDeSujetoAprocesar[0].terminadoDeProcesarPropiedad()
            else:
                    # REGLA 4
                # Categorical objects and subjects of objects or subjects give origin to levels
                # Si no cae en la categoria de medida, entonces es un categorico del verbo
                procesadoEnSujeto.nuevoLelDeNivel(lelDeSujetoAprocesar[0])
                if(not lelDeSujetoAprocesar[0].estaProcesado):
                    procesadoEnSujeto.nuevoLelDeNivelNoProcesado(lelDeSujetoAprocesar[0])
                    lelDeSujetoAprocesar[0].terminadoDeProcesarNivel()

    

    def esArcoMultiple(self, encontradoEnSujeto: EncontradoEnSujeto, level):
        ''' . If o′is plural, then the arc from o to o′is a multiple one.'''
        for simbolo in encontradoEnSujeto.pluralChunks:
            aBuscar = simbolo.text.lower()
            if(self.esLelBuscado(level, aBuscar)):
                return True
            if(self.esLelBuscadoCompuesto(level, aBuscar)):
                return True
        return False

    def esArcoOpcional(self, docNotionLevel, level):
        '''
        If the docNotion  used in n to relate o with o′ suggests that some instances
of o may not be associated to every instance of o′, then the arc from o to o′ is an optional one.
        '''    
           #         Rule 7 deals with expressions of possibility. Although simple analysis
            #could be made using a glossary of modal auxiliaries (e.g., may, might, could,
            #would, should), a more complete analysis would require some epistemic
            #expressions
        pass




    
