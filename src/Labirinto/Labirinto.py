class Labirinto:
    
    def __init__(self, grafo, configuracao):
        self._grafo = grafo
        self._configuracao = configuracao
        self.validar_configuracao_com_grafo()
    
    def validar_configuracao_com_grafo(self):
        numero_vertices = self._grafo.obter_numero_vertices()
        
        if self._configuracao.obter_vertice_entrada() >= numero_vertices:
            raise ValueError("Vértice de entrada fora dos limites do grafo")
        
        if self._configuracao.obter_vertice_saida() >= numero_vertices:
            raise ValueError("Vértice de saída fora dos limites do grafo")
        
        if self._configuracao.obter_posicao_minotauro() >= numero_vertices:
            raise ValueError("Posição inicial do Minotauro fora dos limites do grafo")
    
    def obter_grafo(self):
        return self._grafo
    
    def obter_configuracao(self):
        return self._configuracao