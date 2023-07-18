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

    verboEnDiagrama = ObjetoDiagrama(v.expresion, '',  TipoObjetoDiagrama.HECHO)

    sujetosYObjetosDeVerbo = reglas.encontrarObjetosYsujetosDeVerbo(v.nocion)
    procesadoEnVerbo = reglas.procesarElVerbo(sujetosYObjetosDeVerbo, lelMockeado)


    verboEnDiagrama.prop1 = procesadoEnVerbo.devolverLelsDeMedida()
    
    diagrama.nuevoObjetoDelDiagrama(verboEnDiagrama)
    diagrama.generarLinks(v.expresion, procesadoEnVerbo.lelsCategoricosDeVerbo)                         

lelsAprocesar = procesadoEnVerbo.lelsCategoricosDeVerbo


# True/False are not keywords, they are just built in global constants 
# (that are reassignable like any other variable), 
# so the interpreter has to check what they point to

# 0 and 1 are faster than False and True
while 1:
    hayMasLels = []

    for sujeto in  lelsAprocesar:

        diagrama.nuevoObjetoDelDiagrama(
            ObjetoDiagrama(sujeto.expresion, '', TipoObjetoDiagrama.DIMENSION))

        encontradoEnSujeto  = reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)
        procesadoEnSujeto = reglas.procesarElSujeto(encontradoEnSujeto, lelMockeado)


        diagrama.generarLinks(sujeto.expresion, procesadoEnSujeto.lelsDeNivel )


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






