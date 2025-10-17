class ConfiguracaoLabirinto:
    
    def __init__(
            self, 
            vertice_entrada, 
            vertice_saida, 
            posicao_minotauro, 
            parametro_percepcao, 
            tempo_maximo
        ):
        self._vertice_entrada = vertice_entrada
        self._vertice_saida = vertice_saida
        self._posicao_minotauro = posicao_minotauro
        self._parametro_percepcao = parametro_percepcao
        self._tempo_maximo = tempo_maximo
        self.validar_configuracao()
    
    def validar_configuracao(self):
        if self._vertice_entrada == self._vertice_saida:
            raise ValueError("Vértice de entrada deve ser diferente do vértice de saída")
        
        if self._posicao_minotauro == self._vertice_entrada:
            raise ValueError("Minotauro não pode começar na entrada")
        
        if self._posicao_minotauro == self._vertice_saida:
            raise ValueError("Minotauro não pode começar na saída")
        
        if self._parametro_percepcao < 0:
            raise ValueError("Parâmetro de percepção deve ser não-negativo")
        
        if self._tempo_maximo <= 0:
            raise ValueError("Tempo máximo deve ser positivo")
    
    def obter_vertice_entrada(self):
        return self._vertice_entrada
    
    def obter_vertice_saida(self):
        return self._vertice_saida
    
    def obter_posicao_minotauro(self):
        return self._posicao_minotauro
    
    def obter_parametro_percepcao(self):
        return self._parametro_percepcao
    
    def obter_tempo_maximo(self):
        return self._tempo_maximo