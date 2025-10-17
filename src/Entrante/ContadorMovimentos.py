class ContadorMovimentos:
    
    def __init__(self, valor=0):
        self._valor = valor
    
    def incrementar(self):
        return ContadorMovimentos(self._valor + 1)
    
    def obter_valor(self):
        return self._valor
    
    def eh_menor_ou_igual_a(self, outro_valor):
        return self._valor <= outro_valor
    
    def __repr__(self):
        return f"Movimentos({self._valor})"
