import spacy

from Reglas import Reglas

# Cargar modelo de lenguaje en inglés de Spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("date: A particular day of a month, in a particular year.")

reglas = Reglas()
sujetosYObjetosDeVerbo = reglas.encontrarObjetosYsujetosDeVerbo("date: A particular day of a month, in a particular year.")
print(sujetosYObjetosDeVerbo)
date_token = doc[0] # el primer token de la oración
print("****************")
print(date_token)
candidates = [token for token in doc if token != date_token]

similarities = [(candidate.text, date_token.similarity(candidate)) for candidate in candidates]

similarities_sorted = sorted(similarities, key=lambda x: x[1], reverse=True)

for candidate, score in similarities_sorted:
    print(candidate, score)







