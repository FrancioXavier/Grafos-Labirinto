import random

class ProbabilidadeSobrevivencia:
    
    def __init__(self, valor):
        if not 0 <= valor <= 1:
            raise ValueError("Probabilidade deve estar entre 0 e 1")
        self._valor = valor
    
    def obter_valor(self):
        return self._valor
    
    def __repr__(self):
        return f"Probabilidade({self._valor * 100}%)"


class ResultadoBatalha:
    
    def __init__(self, entrante_sobreviveu):
        self._entrante_sobreviveu = entrante_sobreviveu
    
    def entrante_sobreviveu(self):
        return self._entrante_sobreviveu
    
    def __repr__(self):
        resultado = "VITÓRIA" if self._entrante_sobreviveu else "DERROTA"

        return f"ResultadoBatalha({resultado})"


class SistemaBatalha:
    
    def __init__(self, probabilidade_sobrevivencia):
        self._probabilidade_sobrevivencia = probabilidade_sobrevivencia
    
    def executar_batalha(self):
        sorteio = random.random()
        sobreviveu = sorteio < self._probabilidade_sobrevivencia.obter_valor()

        return ResultadoBatalha(sobreviveu)
    
    def __repr__(self):
        return f"SistemaBatalha({self._probabilidade_sobrevivencia})"
