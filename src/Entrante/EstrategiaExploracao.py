class EstrategiaExploracao:
    
    def __init__(self, grafo, novelo):
        self._grafo = grafo
        self._novelo = novelo
    
    def escolher_proximo_vertice(self, vertice_atual):
        vizinhos = self._grafo.obter_adjacentes(vertice_atual)
        
        for aresta in vizinhos:
            vizinho = aresta.obter_destino()
            if not self._novelo.vertice_foi_visitado(vizinho):
                return vizinho
        
        if not self._novelo.caminho_esta_vazio():
            ultimo_caminho = self._novelo.retroceder_caminho()
            if ultimo_caminho:
                return ultimo_caminho.obter_origem()
        
        return None
    
    def tem_vizinhos_nao_visitados(self, vertice):
        vizinhos = self._grafo.obter_adjacentes(vertice)
        for aresta in vizinhos:
            vizinho = aresta.obter_destino()
            if not self._novelo.vertice_foi_visitado(vizinho):
                return True

        return False
    
    def obter_peso_movimento(self, origem, destino):
        return self._grafo.obter_peso_aresta(origem, destino)
    
    def __repr__(self):
        return "EstrategiaExploracao(DFS + Backtracking)"
