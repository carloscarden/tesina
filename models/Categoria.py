from enum import Enum

''' 
Los símbolos se categorizan en una de cuatro categorías básicas con el fin de especializar la descripción
de los atributos. Las cuatro categorías básicas son: sujeto, objeto, verbo y estado
'''
class Categoria(Enum):
    ''' 
    los verbos son las acciones que realizan los sujetos sobre los objetos.
    '''
    VERBO = 1

    ''' 
     los objetos se corresponden con elementos pasivos
    '''
    OBJETO = 2

    ''' 
    Los sujetos se corresponden con elementos activos dentro del contexto de la aplicación,
    '''
    SUJETO = 3
