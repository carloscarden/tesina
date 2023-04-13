import spacy

from models.Lel import Lel
from models.mockLel import MockLel

from models.termino import Termino
from reglas import Regla

nlp = spacy.load("en_core_web_sm")


reglas = Regla()

m = MockLel()
lelMockeado = m.lelMockeado()

lel4 = Lel(Termino.OBJETO, 'Drug', ''' Medicine or other substance which has a physiological effect when ingested or otherwise introduced into the body according to
its administration mode. The drug is also characterized by an elimination mode''')

               # REGLA 4
#Categorical objects and subjects of verbs give origin to dimensions
encontradoEnSujeto = reglas.encontrarLosObjetosCategoricosDeSujetos(lel4)
procesadoEnSujeto = reglas.procesarElSujeto(encontradoEnSujeto, lelMockeado)

print(procesadoEnSujeto.lelsDePropiedad) 
print([l.expresion for l in procesadoEnSujeto.lelsDeNivel]) 
    


