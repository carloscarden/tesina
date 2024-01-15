from Reglas import Reglas
from models.clasesDiagrama.DiagramasEnVerbo import DiagramasEnVerbo
from models.clasesDiagrama.DiagramasEnSujeto import DiagramasEnSujeto
from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama
from models.mockLel import MockLel
import spacy


nlp = spacy.load("en_core_web_sm")
reglas = Reglas()
m = MockLel()
lelMockeado = m.lelMockeado()

diagrama = Diagrama([], [])

diagramasEnVerbo = DiagramasEnVerbo(diagrama)
diagramasEnSujeto = DiagramasEnSujeto(diagrama)

        # REGLA 1
# Verbs give origin to facts. 
verbos = reglas.recuperarLosVerbos(lelMockeado)

for v in verbos:


    # v should be defined as a fact
    diagramasEnVerbo.nuevoHecho(v)

    # Encontrar todos los Categorical objects and subjects del verbo
    sujetosYObjetosDeVerbo = reglas.encontrarObjetosYsujetosDeVerbo(v.nocion)


    # apply Rule 2 to v, get set Mf of measures, add them to f
    # apply Rule 3 to v, get set Df of dimensions, add them to f
    procesadoEnVerbo = reglas.procesarElVerbo(sujetosYObjetosDeVerbo, lelMockeado)


    diagramasEnVerbo.generarObjetosDelDiagramaPorVerbo(procesadoEnVerbo, v.simbolo)

    v.terminadoDeProcesarVerbo()


lelsAprocesar = procesadoEnVerbo.lelsCategoricosDeVerbo


while 1:
    hayMasLels = []

    for sujeto in  lelsAprocesar:

        diagrama.nuevoObjetoDelDiagrama(
            ObjetoDiagrama(sujeto.simbolo , '', TipoObjetoDiagrama.DIMENSION))

        encontradoEnSujeto  = reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)
        procesadoEnSujeto = reglas.procesarElSujeto(encontradoEnSujeto, lelMockeado)


        diagrama.generarLinks(sujeto.simbolo , procesadoEnSujeto.lelsDeNivel )


    if not hayMasLels:
        break
    else:
        lelsAprocesar = hayMasLels

print("DIAGRAMAS")
for o in diagrama.objetosDelDiagrama:
    print(o.key)
print("**********************************")
print("LINKS")
for l in diagrama.linksDelDiagrama:
    print(l.desde+ " to "+l.hasta)
print("**********************************")






