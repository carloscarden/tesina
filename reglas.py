
from nltk.corpus import wordnet
from models.Lel import Lel
from models.encontradoEnSujeto import EncontradoEnSujeto
from models.procesadoEnSujeto import ProcesadoEnSujeto
from models.procesadoEnVerbo import ProcesadoEnVerbo
from models.termino import Termino
from typing import List

import spacy

nlp = spacy.load("en_core_web_sm")

class Regla:

    def recuperarLosVerbos(self, lels: List[Lel]):
          return [objeto for objeto in lels if objeto.termino == Termino.VERBO]
    
    
    def encontrarObjetosYsujetosDeVerbo(self, nocion):
        notionVerboDoc = nlp(nocion)
        # procesar notion para que me de los objetos y sujetos
        lista_expresiones = self.procesarNotion(notionVerboDoc)
        return lista_expresiones


    def procesarNotion(self, doc):
        # Lista para almacenar los objetos encontrados
        objetos_y_sujetos = []
        # Recorrer los tokens y verificar si son objetos 
        for token in doc:
            # Verificar si el token es un sustantivo
            if token.pos_ == "NOUN" :
                objetos_y_sujetos.append(token.text)
        return objetos_y_sujetos

    def procesarElVerbo(self, sujetosYObjetosDeVerbo, lelMockeado)-> ProcesadoEnVerbo:
        procesadoEnVerbo = ProcesadoEnVerbo([],[])
        for expresion in sujetosYObjetosDeVerbo :
            lelDeVerboAprocesar = list( filter( lambda obj_lel: self.esLelBuscado(obj_lel, expresion) , 
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
        target_words = ["has","according to", "characterized by","manufactured"]

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


    def fraseCompuesta(self, token, doc, target_words):
        if token.i < len(doc) - 1:
            target_phrase = token.text + " " + doc[token.i + 1].text
            return target_phrase in target_words
        return False

    def procesarNounChunk(self, encontradoEnSujeto: EncontradoEnSujeto, noun_chunk):
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

    def fraseCompuesta(self, token, doc, target_words):
        if token.i < len(doc) - 1:
            target_phrase = token.text + " " + doc[token.i + 1].text
            return target_phrase in target_words
        return False


    def procesarElSujeto(self, encontradoEnSujeto: EncontradoEnSujeto, lelMockeado) -> ProcesadoEnSujeto:

        procesadoEnSujeto = ProcesadoEnSujeto([],[],[])
        self.procesarLosObjectsSimples(procesadoEnSujeto, encontradoEnSujeto.objectsSimple, lelMockeado)
        self.procesarLosPalabraDoble(procesadoEnSujeto, encontradoEnSujeto, lelMockeado)

        return procesadoEnSujeto



    def procesarLosObjectsSimples(self, procesadoEnSujeto: ProcesadoEnSujeto, 
                                   objectsSimple, lelMockeado):
        
        for expresion in objectsSimple:
            aBuscar = expresion.text.lower()

            lelDeSujetoAprocesar = list( filter( lambda lel: self.esLelBuscado(lel, aBuscar) , 
                                           lelMockeado))
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

    
    def esLelBuscado(unLel: Lel, expresionAbuscar: str):
        return  unLel.expresion.lower()==  expresionAbuscar and unLel.termino != Termino.VERBO

    
    def procesarLosPalabraDoble(self, procesadoEnSujeto, encontradoEnSujeto):
        return ''
    