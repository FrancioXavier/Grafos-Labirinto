from .Movimentacao import Movimentacao
from Grafos.Grafo import Grafo
import random

class MovimentacaoNormal(Movimentacao):
    def __init__(self, grafo: Grafo):
        self._grafo = grafo

    def mover(self, pos_minotauro: int, pos_entrante: int, percepcao: int):
        adjacentes = self._grafo.obter_adjacentes(pos_minotauro)
        if not adjacentes:
            return pos_minotauro
        
        proximo_vertice = random.choice(adjacentes).obter_destino()

        return proximo_vertice
