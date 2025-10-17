class TempoMaximo:
    
    def __init__(self, valor):
        if valor < 0:
            raise ValueError("Tempo máximo não pode ser negativo")
        self._valor = valor
    
    def obter_valor(self):
        return self._valor
    
    def __repr__(self):
        return f"TempoMaximo({self._valor})"
