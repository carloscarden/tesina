import spacy

from nltk.corpus import wordnet
from spacy.tokens import Span
from models.Lel import Lel

from models.encontradoEnSujeto import EncontradoEnSujeto

nlp = spacy.load("en_core_web_sm")

def fraseCompuesta(token, doc, target_words):
    if token.i < len(doc) - 1:
        target_phrase = token.text + " " + doc[token.i + 1].text
        return target_phrase in target_words
    return False
    
def procesarNounChunk(encontradoEnSujeto: EncontradoEnSujeto, noun_chunk):
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


def encontrarLosObjetosCategoricosDeSujetos(lelsCategoricos: Lel):
    text = ''' Medicine or other substance which has a physiological effect 
    when ingested or otherwise introduced into the body according to its administration mode. 
The drug is also characterized by an elimination mode.  
A model has a capacity and is manufactured in one or more factories'''
    doc = nlp(lelsCategoricos.nocion)

    # Lista de palabras objetivo
    target_words = ["has","according to", "characterized by","manufactured"]

    encontradoEnSujeto = EncontradoEnSujeto([],[], [])


    for token in doc:
        esCompuesta = fraseCompuesta(token, doc, target_words)
        
        if token.text in target_words or fraseCompuesta(token, doc, target_words):
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
                procesarNounChunk(encontradoEnSujeto, noun_chunk)
    return encontradoEnSujeto



lelsDeMedida = []
lelsDeNiveles = []
lelDeobjetosYsujetosDelVerbo = []

               # REGLA 4
#Categorical objects and subjects of verbs give origin to dimensions
encontradoEnSujeto = encontrarLosObjetosCategoricosDeSujetos(lelsDeMedida)
