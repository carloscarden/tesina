

"""El LEL es un glosario
en el cual se definen símbolos (términos o frases), y cada símbolo se define a través
de dos atributos: la noción y los impactos"""

from models.DatosParaProcesoDiagrama import DatosParaProcesoDiagrama
from models.clasesDiagrama.tipoObjetoDiagrama import TipoObjetoDiagrama


class Lel:

    i = 12345

    def __init__(self, categoria: str, simbolo: str, nocion: str):
        self.categoria = categoria

        '''
        símbolos (términos o frases)
        '''
        self.simbolo = simbolo

        ''' 
        La noción describe la denotación, es decir, describe las características intrínsecas 
        y sustanciales del símbolo
        '''
        self.nocion = nocion

        '''
        Datos necesarios para la construccion del diagrama
        '''
        self.datosParaProceso = DatosParaProcesoDiagrama(False, None, None)


    def terminadoDeProcesarVerbo(self):
        self.datosParaProceso.procesadoLel = True
        self.datosParaProceso.tipoObjetoDiagrama = TipoObjetoDiagrama.HECHO

