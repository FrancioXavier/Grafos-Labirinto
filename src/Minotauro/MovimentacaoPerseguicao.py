from .Movimentacao import Movimentacao
from Grafos.Grafo import Grafo

class MovimentacaoPerseguicao(Movimentacao):
    def __init__(self, grafo: Grafo):
        self._grafo = grafo

    def mover(self, pos_minotauro: int, pos_entrante: int, percepcao: int):
        caminho = self._grafo.obter_caminho_minimo(pos_minotauro, pos_entrante)
        
        if len(caminho) > 2:
            return caminho[2]
        elif len(caminho) > 1:
            return caminho[1]
        else:
            return pos_minotauro
