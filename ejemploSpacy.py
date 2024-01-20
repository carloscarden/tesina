import spacy
from ReglasEnVerbo import ReglasEnVerbo

from models.mockLel import MockLel


m = MockLel()
lelMockeado = m.lelMockeado()

reglasVerbo = ReglasEnVerbo()

# REGLA1
# Verbs give origin to facts. 
verbo = reglasVerbo.recuperarLosVerbos(lelMockeado)

#  devuelve :  lel Administer

# Encontrar todos los Categorical objects and subjects del verbo
sujetosYObjetosDeVerbo = reglasVerbo.encontrarObjetosYsujetosDeVerbo(verbo[0].nocion)


# apply Rule 2 to v, get set Mf of measures, add them to f
# apply Rule 3 to v, get set Df of dimensions, add them to f
procesadoEnVerbo = reglasVerbo.procesarElVerbo(sujetosYObjetosDeVerbo, lelMockeado)




