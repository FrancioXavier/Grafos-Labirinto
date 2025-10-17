from .StatusEntrante import StatusEntrante
from .ContadorMovimentos import ContadorMovimentos
from .SistemaBatalha import SistemaBatalha, ProbabilidadeSobrevivencia, ResultadoBatalha
from .EstrategiaExploracao import EstrategiaExploracao
from .TempoMaximo import TempoMaximo
from NoveloLa.NoveloLa import NoveloLa

class Entrante:
    
    def __init__(self, posicao_inicial, grafo):
        self._posicao_atual = posicao_inicial
        self._grafo = grafo
        self._novelo = NoveloLa()
        self._estrategia = EstrategiaExploracao(grafo, self._novelo)
        self._status = StatusEntrante.criar_explorando()
        self._movimentos = ContadorMovimentos()
        self._sistema_batalha = SistemaBatalha(ProbabilidadeSobrevivencia(0.01))
        
        self._novelo.marcar_vertice_como_visitado(posicao_inicial)
    
    def obter_posicao_atual(self):
        return self._posicao_atual
    
    def obter_status(self):
        return self._status
    
    def obter_contador_movimentos(self):
        return self._movimentos
    
    def esta_vivo(self):
        return self._status.esta_vivo()
    
    def mover_para_proximo_vertice(self):
        if not self._status.esta_explorando():
            return False
        
        proximo_vertice = self._estrategia.escolher_proximo_vertice(self._posicao_atual)
        
        if proximo_vertice is None:
            return False
        
        peso = self._estrategia.obter_peso_movimento(self._posicao_atual, proximo_vertice)
        self._novelo.adicionar_ao_caminho(self._posicao_atual, proximo_vertice, peso)
        self._posicao_atual = proximo_vertice
        self._novelo.marcar_vertice_como_visitado(proximo_vertice)
        self._movimentos = self._movimentos.incrementar()
        
        return True
    
    def verificar_encontrou_saida(self, vertice_saida):
        if self._posicao_atual == vertice_saida:
            self._status = StatusEntrante.criar_escapou()
            return True

        return False
    
    def enfrentar_batalha(self):
        resultado = self._sistema_batalha.executar_batalha()
        
        if resultado.entrante_sobreviveu():
            self._status = StatusEntrante.criar_vitoria()
        else:
            self._status = StatusEntrante.criar_morto()
        
        return resultado
    
    def verificar_tempo_esgotado(self, tempo_maximo):
        if not self._movimentos.eh_menor_ou_igual_a(tempo_maximo):
            self._status = StatusEntrante.criar_tempo_esgotado()
            return True
        return False
    
    def obter_estatisticas(self):
        return {
            'posicao_atual': self._posicao_atual,
            'vertices_explorados': self._novelo.quantidade_vertices_visitados(),
            'movimentos_realizados': self._movimentos.obter_valor(),
            'status': self._status.obter_estado(),
            'vivo': self._status.esta_vivo()
        }
    
    def obter_sequencia_visitados(self):
        historico = self._novelo.obter_historico_completo()
        if not historico:
            return [self._posicao_atual]
        
        sequencia = [historico[0].obter_origem()]
        for passo in historico:
            sequencia.append(passo.obter_destino())
            
        return sequencia

    def __repr__(self):
        return f"Entrante(pos={self._posicao_atual}, mov={self._movimentos}, {self._status})"
