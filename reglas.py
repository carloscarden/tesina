
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

from typing import List



nlp = spacy.load("en_core_web_sm")


class Regla:

    def recuperarLosVerbos(self, lels: List[Lel]):
          return [objeto for objeto in lels if objeto.categoria == Categoria.VERBO]
    
    
    def encontrarObjetosYsujetosDeVerbo(self, nocion: str):
        notionVerboDoc = nlp(nocion)
        # procesar notion para que me de los objetos y sujetos
        lista_simboloes = self.procesarNotion(notionVerboDoc)
        return lista_simboloes


    def procesarNotion(self, doc: Doc) -> List[str]:
        # Lista para almacenar los objetos encontrados
        objetos_y_sujetos = []
        # Recorrer los tokens y verificar si son objetos 
        for token in doc:
            # Verificar si el token es un sustantivo
            if token.pos_ == "NOUN" :
                objetos_y_sujetos.append(token.text)
        return objetos_y_sujetos

    def procesarElVerbo(self, sujetosYObjetosDeVerbo: List[str], lelMockeado: List[Lel])-> ProcesadoEnVerbo:
        procesadoEnVerbo = ProcesadoEnVerbo([],[])
        for simbolo in sujetosYObjetosDeVerbo :
            # Encontrar el LEL correspondiente
            lelDeVerboAprocesar = list( filter( lambda obj_lel: self.esLelBuscado(obj_lel, simbolo) , 
                                           lelMockeado))
            if lelDeVerboAprocesar:
                doc = nlp(lelDeVerboAprocesar[0].nocion)
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
        return procesadoEnVerbo

    def es_medida(self, palabra):
        sinonimos = set()
        '''
    En Spacy, lemma_ es un atributo de los tokens que devuelve la forma base o lema de la palabra. 
    Es decir, la forma canónica de la palabra a la que pertenece el token, sin conjugaciones verbales,
      ni desinencias de género o número en sustantivos y adjetivos.

    Por ejemplo, el lemma de los verbos "corrió", "corremos", "corriendo" y "correrán" es "correr". 
    El lemma de los sustantivos "autos", "automóviles" y "coches" es "auto". 
    Esto es útil para llevar a cabo análisis de texto, ya que a menudo queremos agrupar diferentes 
    formas de la misma palabra en una sola categoría o término.
    '''
        for syn in wordnet.synsets(palabra, lang='eng'):
            for lemma in syn.lemmas(lang='eng'):
                sinonimos.add(lemma.name())
        sinonimos.add(palabra)
        medidas = {'amount', 'size', 'capacity',
                  'volume', 'length', 'width',
                  'amplitude', 'density', 'extension'}
        return any(medida in sinonimos for medida in medidas)



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


    def fraseCompuesta(self, token: Token, doc: Doc, target_words: List[str]) -> bool:
        if token.i < len(doc) - 1:
            target_phrase = token.text + " " + doc[token.i + 1].text
            return target_phrase in target_words
        return False

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

    
    def esLelBuscado(self, unLel: Lel, simboloAbuscar: str):
        return  unLel.simbolo.lower()==  simboloAbuscar and unLel.categoria != Categoria.VERBO


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

    
    def procesarLosPalabraDoble(self, procesadoEnSujeto, nounChunks, lelMockeado):
        for nc in nounChunks:
            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscadoCompuesto(lel, nc) , 
                                           lelMockeado))
            self.tipoDeLelQueEsElSujeto(lelDeSujetoAprocesar, procesadoEnSujeto)                               


    def esLelBuscadoCompuesto(self, unLel: Lel, simboloAbuscar):
        completo = " ".join([ n.text for n in simboloAbuscar]).strip()
        ultimo  = simboloAbuscar[-1].text.strip()
        return ( unLel.simbolo.lower().strip() ==  completo.lower() and unLel.categoria != Categoria.VERBO ) or \
               ( unLel.simbolo.lower().strip() ==  ultimo.lower() and unLel.categoria != Categoria.VERBO )
    