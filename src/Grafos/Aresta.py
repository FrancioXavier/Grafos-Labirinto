class Aresta:
    
    def __init__(self, destino, peso):
        self._destino = destino
        self._peso = peso
    
    def obter_destino(self):
        return self._destino
    
    def obter_peso(self):
        return self._peso