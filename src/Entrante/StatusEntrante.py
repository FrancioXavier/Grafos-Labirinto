class StatusEntrante:
    EXPLORANDO = "EXPLORANDO"
    ESCAPOU = "ESCAPOU"
    MORTO = "MORTO"
    VITORIA = "VITORIA"
    TEMPO_ESGOTADO = "TEMPO_ESGOTADO"
    
    def __init__(self, estado):
        self._estado = estado
    
    @classmethod
    def criar_explorando(cls):
        return cls(cls.EXPLORANDO)
    
    @classmethod
    def criar_escapou(cls):
        return cls(cls.ESCAPOU)
    
    @classmethod
    def criar_morto(cls):
        return cls(cls.MORTO)
    
    @classmethod
    def criar_vitoria(cls):
        return cls(cls.VITORIA)
    
    @classmethod
    def criar_tempo_esgotado(cls):
        return cls(cls.TEMPO_ESGOTADO)
    
    def obter_estado(self):
        return self._estado
    
    def esta_vivo(self):
        return self._estado not in [self.MORTO, self.TEMPO_ESGOTADO]
    
    def esta_explorando(self):
        return self._estado == self.EXPLORANDO
    
    def __repr__(self):
        return f"Status({self._estado})"
