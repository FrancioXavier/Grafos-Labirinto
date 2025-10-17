from Labirinto.Labirinto import Labirinto
from Configuracao.ConfiguracaoLabirinto import ConfiguracaoLabirinto
from Grafos.Grafo import Grafo

class ConstrutorLabirinto:
    
    def __init__(self, dados_entrada):
        self._dados = dados_entrada
    
    def construir(self):
        grafo = self._construir_grafo()
        configuracao = self.construir_configuracao()

        return Labirinto(grafo, configuracao)
    
    def _construir_grafo(self):
        grafo = Grafo(self._dados['numero_vertices'])
        
        for origem, destino, peso in self._dados['arestas']:
            grafo.adicionar_aresta(origem, destino, peso)
        
        return grafo
    
    def construir_configuracao(self):
        return ConfiguracaoLabirinto(
            self._dados['vertice_entrada'],
            self._dados['vertice_saida'],
            self._dados['posicao_minotauro'],
            self._dados['parametro_percepcao'],
            self._dados['tempo_maximo']
        )