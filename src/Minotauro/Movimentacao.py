from abc import ABC, abstractmethod

class Movimentacao(ABC):
    @abstractmethod
    def mover(self, pos_minotauro: int, pos_entrante: int, percepcao: int):
        pass
