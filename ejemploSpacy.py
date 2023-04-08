import spacy

from nltk.corpus import wordnet

nlp = spacy.load("en_core_web_sm")


def encontrarLosObjetosCategoricosDeSujetos(lelsCategoricos):
    text = '''The car has a red color'''

    doc = nlp(text)

    # Lista de palabras objetivo
    target_words = ["has", "belongs", "comprised", "covered", "incorporated", "involves"]

    for token in doc:
        if token.text in target_words:
            print(token.text)
            # Encuentra el sujeto y el objeto de la relación
            subject = [w for w in token.head.lefts if w.dep_ == "nsubj"]
            print(subject)
            obj = [w for w in token.rights if w.dep_ == "dobj" or w.dep_ == "pobj"]

            # Maneja las preposiciones
            if not obj:
                obj = [w for w in token.rights if w.dep_ == "prep"]
                if obj:
                    obj = [w for w in obj[0].rights if w.dep_ == "pobj"]
            if subject and obj:
                print(f"{subject[0]} {token.text} {obj[0]}")
    return []

lelsDeMedida = []
lelsDeNiveles = []
lelDeobjetosYsujetosDelVerbo = []

               # REGLA 4
#Categorical objects and subjects of verbs give origin to dimensions
lelsDeNiveles = encontrarLosObjetosCategoricosDeSujetos(lelsDeMedida)

