
from spacy.tokens import Doc

"""El LEL es un glosario
en el cual se definen símbolos (términos o frases), y cada símbolo se define a través
de dos atributos: la noción y los impactos"""

class DatosParaProcesoDiagrama:

    i = 12345


    def __init__(self, procesado: bool, docNotion: Doc, unTipoObjetoDiagrama: str):
        # si el lel se proceso o no
        self.procesadoLel = procesado

        self.docNotion = docNotion

        self.tipoObjetoDiagrama =  unTipoObjetoDiagrama



    def getDocNotion(self, nocion, nlp):
        if(self.docNotion):
            return self.docNotion
        
        self.docNotion = nlp(nocion)
        return self.docNotion