
import spacy


from spacy.language import Language
from spacy.tokens import Token
from spacy.tokens import Doc
from spacy.tokens import Span

from nltk.corpus import wordnet


from models.Lel import Lel
from models.Categoria import Categoria

from typing import List



nlp = spacy.load("en_core_web_sm")


class Reglas:


    def procesarNotion(self, doc: Doc) -> List[str]:
        # Lista para almacenar los objetos encontrados
        objetos_y_sujetos = []
        # Recorrer los tokens y verificar si son objetos 
        for token in doc:
            # Verificar si el token es un sustantivo
            if token.pos_ == "NOUN" :
                objetos_y_sujetos.append(token.text)
        return objetos_y_sujetos


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


    def fraseCompuesta(self, token: Token, doc: Doc, target_words: List[str]) -> bool:
        if token.i < len(doc) - 1:
            target_phrase = token.text + " " + doc[token.i + 1].text
            return target_phrase in target_words
        return False

    
    def esLelBuscado(self, unLel: Lel, simboloAbuscar: str):
        ''' Dado un string se fija si el simbolo del lel coincide y es distinto de un verbo'''
        return  unLel.simbolo.lower()==  simboloAbuscar and unLel.categoria != Categoria.VERBO

    
    def esLelBuscadoCompuesto(self, unLel: Lel, simboloAbuscar):
        completo = " ".join([ n.text for n in simboloAbuscar]).strip()
        ultimo  = simboloAbuscar[-1].text.strip()
        return ( unLel.simbolo.lower().strip() ==  completo.lower() and unLel.categoria != Categoria.VERBO ) or \
               ( unLel.simbolo.lower().strip() ==  ultimo.lower() and unLel.categoria != Categoria.VERBO )
    

