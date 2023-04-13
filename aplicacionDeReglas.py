from models.clasesDiagrama.diagrama import Diagrama
from models.clasesDiagrama.objetoDiagrama import ObjetoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama
from models.mockLel import MockLel
from models.termino import Termino
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




for sujeto in  procesadoEnVerbo.lelsCategoricosDeVerbo:

    diagrama.nuevoObjetoDelDiagrama(ObjetoDiagrama(sujeto.expresion, '', TipoObjetoDiagrama.DIMENSION))


    encontradoEnSujeto  = reglas.encontrarLosObjetosCategoricosDeSujetos(sujeto)
    procesadoEnSujeto = reglas.procesarElSujeto(encontradoEnSujeto, lelMockeado)


    diagrama.cargarLasPropiedades(sujeto, procesadoEnSujeto.lelsDePropiedad)
    diagrama.cargarLosNiveles(sujeto, procesadoEnSujeto.lelsDeNivel )





