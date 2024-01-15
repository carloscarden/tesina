
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
        doc = nlp(lelsCategoricos.nocion)

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
                    self.procesarNounChunk(encontradoEnSujeto, noun_chunk)
        return encontradoEnSujeto



    def procesarNounChunk(self, encontradoEnSujeto: EncontradoEnSujeto, noun_chunk: Span ):
        # Crear lista de palabras a eliminar
        stop_words = ["its", "an", "a"]

        for nc in noun_chunk:
            if(nc.tag_ in ["NNS", "NNPS"]):
                encontradoEnSujeto.nuevoPlural(nc)
                return
        sinPreposiciones = [t for t in noun_chunk if t.text.lower() not in stop_words]
        if(len(sinPreposiciones) > 1):
            encontradoEnSujeto.nuevoNounChunk(sinPreposiciones)
        else:
            encontradoEnSujeto.nuevoObjetoSimple(sinPreposiciones[0])


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
            doc = nlp(lelDeSujetoAprocesar[0].nocion)
            medidas = [tok.text for tok in doc if self.es_medida(tok.text)]
            if(len(medidas)>0):
                     #Rule 5. 
                # Numerical objects and subjects of objects or subjects give origin to properties.
                # buscar entre los objetos y sujetos del notion un objeto numerico
                procesadoEnSujeto.nuevoLelDePropiedad(lelDeSujetoAprocesar[0])
            else:
                    # REGLA 4
                # Categorical objects and subjects of objects or subjects give origin to levels
                # Si no cae en la categoria de medida, entonces es un categorico del verbo
                procesadoEnSujeto.nuevoLelDeNivel(lelDeSujetoAprocesar[0])

    

    