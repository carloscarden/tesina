import spacy

from nltk.corpus import wordnet

nlp = spacy.load("en_core_web_sm")

def fraseCompuesta(token, doc, target_words):
    if token.i < len(doc) - 1:
        target_phrase = token.text + " " + doc[token.i + 1].text
        return target_phrase in target_words
    return False
    

def encontrarLosObjetosCategoricosDeSujetos(lelsCategoricos):
    text = '''Medicine or other substance which has a physiological effect when ingested or otherwise 
    introduced into the body has its administration mode. The drug has an elimination mode.
'''
    doc = nlp(text)

    # Lista de palabras objetivo
    target_words = ["has", "according to", "characterized by"]

    for token in doc:
        
        if token.text in target_words or fraseCompuesta(token, doc, target_words):
            print(token.text)
            # Encuentra el sujeto y el objeto de la relación
            subject = [w for w in token.head.lefts if w.dep_ == "nsubj"]
            obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]
            

            print(subject)

            # Busca el objeto en la lista de sustantivos y adjetivos a la derecha
            if not obj:
                obj = [w for w in token.rights if w.dep_ == "amod" or w.dep_ == "nsubj"]
            
            # Maneja las preposiciones
            if not obj:
                obj = [w for w in token.rights if w.dep_ == "prep"]
                if obj:
                    obj = [w for w in obj[0].rights if w.dep_ == "pobj"]
            if obj:
                # Crear lista de palabras a eliminar
                stop_words = ["its", "an", "a"]
                # Find noun chunks that contain the object
                noun_chunk = next((nc for nc in doc.noun_chunks if nc.root == obj[0]), None)
                print('sin mierdas', [t for t in noun_chunk if t.text.lower() not in stop_words])
                if noun_chunk:
                    print(f" {noun_chunk}")
                else:
                    print(f" {obj[0]}")
    return []



lelsDeMedida = []
lelsDeNiveles = []
lelDeobjetosYsujetosDelVerbo = []

               # REGLA 4
#Categorical objects and subjects of verbs give origin to dimensions
lelsDeNiveles = encontrarLosObjetosCategoricosDeSujetos(lelsDeMedida)

   
                         



