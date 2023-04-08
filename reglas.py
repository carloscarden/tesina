
from nltk.corpus import wordnet
from termino import Termino
import spacy

nlp = spacy.load("en_core_web_sm")

class Regla:

    def regla1(lels):
          return [objeto for objeto in lels if objeto.termino == Termino.VERBO]
    
    
    def encontrarObjetosYsujetos(self, nocion, arreglo_objetos_lel):
        notionVerboDoc = nlp(nocion)
        # procesar notion para que me de los objetos y sujetos
        lista_expresiones = self.procesarNotion(notionVerboDoc)
        objetosYsujetos = []
        for expresion in lista_expresiones:
            for obj_lel in arreglo_objetos_lel:
                if obj_lel.expresion.lower()== expresion.lower() and obj_lel.termino != Termino.VERBO:
                    objetosYsujetos.append(obj_lel)
        return objetosYsujetos


    def procesarNotion(self, doc):
        # Lista para almacenar los objetos encontrados
        objetos_y_sujetos = []
        # Recorrer los tokens y verificar si son objetos 
        for token in doc:
            # Verificar si el token es un sustantivo
            if token.pos_ == "NOUN" :
                objetos_y_sujetos.append(token.text)
        return objetos_y_sujetos
    
    def encontrarLosObjetosNumericos(self, lelDeobjetosYsujetosDelVerbo):
        lelsDeMedida = []
        for lel in lelDeobjetosYsujetosDelVerbo:
            doc = nlp(lel.nocion)
            medidas = [tok.text for tok in doc if self.es_medida(tok.text)]
            if(len(medidas)>0):
                lelsDeMedida.append(lel)
        return lelsDeMedida
    
    def es_medida(palabra):
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
        for syn in wordnet.synsets(palabra, lang='spa'):
            for lemma in syn.lemmas(lang='spa'):
                sinonimos.add(lemma.name())
                sinonimos.add(palabra)
                medidas = {'cantidad', 'tamaño', 'capacidad', 
               'volumen', 'longitud', 'anchura',  
               'amplitud', 'densidad', 'extensión'}
        return any(medida in sinonimos for medida in medidas)

    def dameCategoricosDeVerbos(self, lelDeobjetosYsujetosDelVerbo, lelsDeMedida):
        return []

    

    def dameCategoricosDeSujetos(self, lelSujeto, lelsCategoricosDeVerbo):
        text = '''A car has a model. A model belongs to one segment. 
    A segment is comprised by different car models according to their size, use, and capacity.'''
        doc = nlp(text)
        # Lista de palabras objetivo
        target_words = ["has", "belongs", "comprised", "covered", "incorporated", "involves"]

        for token in doc:
            if token.text in target_words:
                # Encuentra el sujeto y el objeto de la relación
                subject = [w for w in token.head.lefts if w.dep_ == "nsubj"]
                obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]

                # Maneja las preposiciones
                if not obj:
                    obj = [w for w in token.rights if w.dep_ == "prep"]
                    if obj:
                        obj = [w for w in obj[0].rights if w.dep_ == "pobj"]
                if subject and obj:
                    print(f"{subject[0]} {token.text} {obj[0]}")
    

