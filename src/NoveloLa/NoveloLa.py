from .CaminhoPercorrido import CaminhoPercorrido

class NoveloLa:
    
    def __init__(self):
        self._vertices_visitados = set()
        self._pilha_caminho = []
    
    def marcar_vertice_como_visitado(self, vertice):
        self._vertices_visitados.add(vertice)
    
    def vertice_foi_visitado(self, vertice):
        return vertice in self._vertices_visitados
    
    def adicionar_ao_caminho(self, origem, destino, peso):
        caminho = CaminhoPercorrido(origem, destino, peso)
        self._pilha_caminho.append(caminho)
    
    def retroceder_caminho(self):
        if self._pilha_caminho:
            return self._pilha_caminho.pop()

        return None
    
    def obter_posicao_atual(self):
        if self._pilha_caminho:
            return self._pilha_caminho[-1].obter_destino()
        return None
    
    def caminho_esta_vazio(self):
        return len(self._pilha_caminho) == 0
    
    def quantidade_vertices_visitados(self):
        return len(self._vertices_visitados)
    
    def obter_historico_completo(self):
        return self._pilha_caminho.copy()
    
    def __repr__(self):
        return f"NoveloLa({self.quantidade_vertices_visitados()} vértices explorados)"
