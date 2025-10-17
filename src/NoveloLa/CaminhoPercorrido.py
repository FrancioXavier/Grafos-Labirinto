class CaminhoPercorrido:
    
    def __init__(self, origem, destino, peso):
        self._origem = origem
        self._destino = destino
        self._peso = peso
    
    def obter_origem(self):
        return self._origem
    
    def obter_destino(self):
        return self._destino
    
    def obter_peso(self):
        return self._peso
    
    def __repr__(self):
        return f"Caminho({self._origem} -> {self._destino})"
