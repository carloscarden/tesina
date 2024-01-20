from AplicadorDeReglasSujeto import AplicadorDeReglasSujeto
from AplicadorDeReglasVerbo import AplicadorDeReglasVerbo
from models.clasesDiagrama.diagrama import Diagrama
from models.mockLel import MockLel


m = MockLel()
lelMockeado = m.lelMockeado()

diagrama = Diagrama([], [])



aplicadorDeReglasVerbo = AplicadorDeReglasVerbo(diagrama) 
lelsCategoricosDeVerbo = aplicadorDeReglasVerbo.aplicarReglasDeVerbo(lelMockeado)

aplicadorDeReglasSujeto = AplicadorDeReglasSujeto(diagrama)
aplicadorDeReglasSujeto.aplicarReglasDeSujeto(lelsCategoricosDeVerbo, lelMockeado)

print(diagrama)
