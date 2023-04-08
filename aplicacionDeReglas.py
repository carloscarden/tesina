

from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama
from models.mockLel import MockLel

from reglas import Regla


def imprimirLelsDeMedida(lelsDeMedida):
    for lelDeNivel in lelsDeMedida:
        print(lelDeNivel)

def imprimirLelsDeNivel(lelsDeNiveles):
    for l in lelsDeNiveles:
        print('**************************')
        print(l.expresion)
        print(l.termino)
        print(l.nocion)
        print('**************************')

m = MockLel()
lelMockeado = m.lelMockeado()

objetosDeDiagrama = []
linksDelDiagrama = []

lelsDeMedida = []
lelsCategoricosDeVerbo = []
lelsDeNiveles = []


reglas = Regla()

def generarLinks(linksDelDiagrama, lelsCategoricosDeVerbo):
    return ""

# REGLA 1
# Verbs give origin to facts. 
verbos = reglas.regla1(lelMockeado)

for v in verbos:
    verboEnDiagrama = ObjetoDiagrama(v.expresion, '',  TipoObjetoDiagrama.HECHO)

    lelDeobjetosYsujetosDelVerbo = reglas.encontrarObjetosYsujetos(v.nocion, lelMockeado)

                    # REGLA 2
    # Numerical objects and subjects of verbs give origin to measures.
    # buscar entre los objetos y sujetos del notion un objeto numerico
    lelsDeMedida = reglas.encontrarLosObjetosNumericos(lelDeobjetosYsujetosDelVerbo)

    if(lelsDeMedida):
        verboEnDiagrama.prop1 = lelsDeMedida[0].expresion
    
    objetosDeDiagrama.append(verboEnDiagrama)

                    # REGLA 3
    # Categorical objects and subjects of verbs give origin to dimensions
    # Sacar de todos los objetos y sujetos los objetos numericos
    lelsCategoricosDeVerbo = reglas.\
                              dameCategoricosDeVerbos(lelDeobjetosYsujetosDelVerbo, lelsDeMedida)
    generarLinks(linksDelDiagrama, lelsCategoricosDeVerbo)
    



for sujeto in lelsCategoricosDeVerbo:
                  # REGLA 4
    #Categorical objects and subjects of verbs give origin to dimensions
    lelsDeNiveles = reglas.dameCategoricosDeSujetos(sujeto, lelsCategoricosDeVerbo)
    linksDelDiagrama.append(lelsDeNiveles)

imprimirLelsDeNivel(lelsDeNiveles)


