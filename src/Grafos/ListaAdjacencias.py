class ListaAdjacencias:
    
    def __init__(self):
        self._adjacencias = []
    
    def adicionar(self, aresta):
        self._adjacencias.append(aresta)
    
    def obter_todas(self):
        return self._adjacencias
    
    def existe_adjacencia_para(self, vertice):
        for aresta in self._adjacencias:
            if aresta.obter_destino() == vertice:
                return True

        return False
    
    def obter_peso_para(self, vertice):
        for aresta in self._adjacencias:
            if aresta.obter_destino() == vertice:
                return aresta.obter_peso()

        return None