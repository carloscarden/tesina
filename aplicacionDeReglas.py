from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama
from models.mockLel import MockLel
import spacy
from reglas import Regla


nlp = spacy.load("en_core_web_sm")
reglas = Regla()
m = MockLel()
lelMockeado = m.lelMockeado()

diagrama = Diagrama([], [])

        # REGLA 1
# Verbs give origin to facts. 
verbos = reglas.recuperarLosVerbos(lelMockeado)

for v in verbos:

    verboEnDiagrama = ObjetoDiagrama(v.simbolo, '',  TipoObjetoDiagrama.HECHO)



    # Encontrar todos los Categorical objects and subjects del verbo
    sujetosYObjetosDeVerbo = reglas.encontrarObjetosYsujetosDeVerbo(v.nocion)


    # apply Rule 2 to v, get set Mf of measures, add them to f
    # apply Rule 3 to v, get set Df of dimensions, add them to f
    procesadoEnVerbo = reglas.procesarElVerbo(sujetosYObjetosDeVerbo, lelMockeado)


    # all the elements in lelsDeMedida should be defined as measures of the
    # fact corresponding to v
    verboEnDiagrama.prop1 = procesadoEnVerbo.devolverLelsDeMedida()
    
    diagrama.nuevoObjetoDelDiagrama(verboEnDiagrama)


    # all the elements in lelsDeMedida should be defined as measures of the
    # fact corresponding to v
    diagrama.generarLinks(v.simbolo, procesadoEnVerbo.lelsCategoricosDeVerbo)                         

lelsAprocesar = procesadoEnVerbo.lelsCategoricosDeVerbo


# True/False are not keywords, they are just built in global constants 
# (that are reassignable like any other variable), 
# so the interpreter has to check what they point to

# 0 and 1 are faster than False and True
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






