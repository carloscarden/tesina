import spacy

from mockLel import MockLel
from nltk.corpus import wordnet
from termino import Termino

nlp = spacy.load("es_core_news_sm")

def procesarNotion(doc):
    # Lista para almacenar los objetos encontrados
    objetos_y_sujetos = []
    # Recorrer los tokens y verificar si son objetos 
    for token in doc:
        # Verificar si el token es un sustantivo 
        if token.pos_ == "NOUN" :
            objetos_y_sujetos.append(token.text)
    return objetos_y_sujetos


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

def encontrarObjetosYsujetos(lista_expresiones, arreglo_objetos_lel):
    objetosYsujetos = []

    for expresion in lista_expresiones:
        for obj_lel in arreglo_objetos_lel:
            if obj_lel.expresion.lower()== expresion.lower() and obj_lel.termino != Termino.VERBO:
                objetosYsujetos.append(obj_lel)
    return objetosYsujetos

def encontrarLosObjetosNumericos(lelDeobjetosYsujetosDelVerbo):
    lelsDeMedida = []
    for lel in lelDeobjetosYsujetosDelVerbo:
        doc = nlp(lel.nocion)
        medidas = [tok.text for tok in doc if es_medida(tok.text)]
        if(len(medidas)>0):
            lelsDeMedida.append(lel)
    return lelsDeMedida

def encontrarLosObjetosCategoricos(lelsDeMedida, lelDeobjetosYsujetosDelVerbo):
    return []

m = MockLel()
lelMockeado = m.lelMockeado()

lelsDeMedida = []
lelsDeNiveles = []
# REGLA 1
# Verbs give origin to facts. 
verbos = [objeto for objeto in lelMockeado if objeto.termino == Termino.VERBO]

for v in verbos:
    notionVerboDoc = nlp(v.nocion)

    # procesar notion para que me de los objetos y sujetos
    listaExpresiones = procesarNotion(notionVerboDoc)
    lelDeobjetosYsujetosDelVerbo = encontrarObjetosYsujetos(listaExpresiones, lelMockeado)

                    # REGLA 2
    # Numerical objects and subjects of verbs give origin to measures.
    # buscar entre los objetos y sujetos del notion un objeto numerico
    lelsDeMedida = encontrarLosObjetosNumericos(lelDeobjetosYsujetosDelVerbo)

               # REGLA 3
    #Categorical objects and subjects of verbs give origin to dimensions
    lelsDeNiveles = encontrarLosObjetosCategoricos(lelsDeMedida, lelDeobjetosYsujetosDelVerbo)

for lelDeNivel in lelsDeNiveles:
    print(lelDeNivel)

for l in lelsDeMedida:
    print('**************************')
    print(l.expresion)
    print(l.termino)
    print(l.nocion)
    print('**************************')
