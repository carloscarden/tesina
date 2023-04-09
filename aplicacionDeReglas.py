from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama
from models.mockLel import MockLel

from reglas import Regla



def cargarLosNivelesAlDiagrama(sujeto, lelsDeNiveles):
    return ''

def cargarLasPropiedadesAlDiagrama(sujeto, lelsDePropiedades, objetosDelDiagrama):
    for lel in lelsDePropiedades:
        print(lel)

    return ''

reglas = Regla()
m = MockLel()
lelMockeado = m.lelMockeado()

diagrama = Diagrama([], [])

lelsDeMedida = []
lelsCategoricosDeVerbo = []
lelDeobjetosYsujetosDeSujetos  = []
lelsDeNivel = []

verbos = reglas.recuperarLosVerbos(lelMockeado)

for v in verbos:

                    # REGLA 1
    # Verbs give origin to facts. 
    verboEnDiagrama = ObjetoDiagrama(v.expresion, '',  TipoObjetoDiagrama.HECHO)

    lelDeobjetosYsujetosDelVerbo = reglas.encontrarObjetosYsujetos(v.nocion, lelMockeado)

                    # REGLA 2
    # Numerical objects and subjects of verbs give origin to measures.
    # buscar entre los objetos y sujetos del notion un objeto numerico
    lelsDeMedida = reglas.encontrarLosObjetosNumericos(lelDeobjetosYsujetosDelVerbo)

    if(lelsDeMedida):
        verboEnDiagrama.prop1 = lelsDeMedida[0].expresion
    
    diagrama.nuevoObjetoDelDiagrama(verboEnDiagrama)

                    # REGLA 3
    # Categorical objects and subjects of verbs give origin to dimensions
    # Sacar de todos los objetos y sujetos los objetos numericos
    lelsCategoricosDeVerbo = reglas.\
                              dameCategoricosDeVerbos(lelDeobjetosYsujetosDelVerbo, lelsDeMedida)

    diagrama.generarLinks(v.expresion, lelsCategoricosDeVerbo)                         





for sujeto in lelsCategoricosDeVerbo:
    nuevaDimension = ObjetoDiagrama(sujeto.expresion, '', TipoObjetoDiagrama.DIMENSION)
    diagrama.nuevoObjetoDelDiagrama(nuevaDimension)

    lelDeobjetosYsujetosDeSujetos  = reglas.dameSujetosDeSujetos(sujeto, lelsCategoricosDeVerbo)

                   #Rule 5. 
    # Numerical objects and subjects of objects or subjects give origin to properties.
    lelsDePropiedades = reglas.encontrarLosObjetosNumericos(lelDeobjetosYsujetosDeSujetos)
    diagrama.cargarLasPropiedades(sujeto, lelsDePropiedades)


                  # REGLA 4
    # Categorical objects and subjects of objects or subjects give origin to levels
    lelsDeNivel = reglas.dameLosNiveles(lelDeobjetosYsujetosDeSujetos, lelsDePropiedades)
    cargarLosNivelesAlDiagrama(sujeto, lelsDeNivel )



