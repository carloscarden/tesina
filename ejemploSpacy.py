import spacy
from numpy import asarray

from models.Lel import Lel
from models.mockLel import MockLel

from models.termino import Termino
from reglas import Regla

nlp = spacy.load('en_core_web_md')

# Obtener los vectores de las palabras "day" y "hour"
day_vector = nlp("day").vector
hour_vector = nlp("hour").vector

# Calcular la similitud semántica entre "day" y otras palabras
similar_words = []
print(len(nlp.vocab))
for word in nlp.vocab:
    if word.has_vector and word.is_lower and word.is_alpha:
        similarity_day = nlp("day").similarity(word)
        similarity_hour = nlp("hour").similarity(word)
        if similarity_day > 0.6 and similarity_hour > 0.6:
            similar_words.append(word.text)

# Imprimir las palabras similares encontradas
print(similar_words)





