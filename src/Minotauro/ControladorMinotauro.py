from .Minotauro import Minotauro
from .MovimentacaoNormal import MovimentacaoNormal
from .MovimentacaoPerseguicao import MovimentacaoPerseguicao
from Grafos.Grafo import Grafo

class ControladorMinotauro:
    def __init__(self, minotauro: Minotauro, grafo: Grafo):
        self._minotauro = minotauro
        self._grafo = grafo
        self._mov_normal = MovimentacaoNormal(grafo)
        self._mov_perseguicao = MovimentacaoPerseguicao(grafo)
        self._momento_deteccao = None

    def obter_momento_deteccao(self):
        return self._momento_deteccao

    def mover(self, pos_entrante: int, percepcao: int, tempo_atual: int):
        distancias = self._minotauro._distancias
        pos_minotauro = self._minotauro.obter_posicao_atual()

        if distancias[pos_entrante][pos_minotauro] <= percepcao:
            if not self._minotauro.esta_perseguindo():
                self._minotauro.iniciar_perseguicao()
                self._momento_deteccao = tempo_atual
                self._minotauro.limpar_caminho_perseguicao()
                self._minotauro.adicionar_ao_caminho_perseguicao(self._minotauro.obter_posicao_atual())
        else:
            self._minotauro.parar_perseguicao()

        if self._minotauro.esta_perseguindo():
            nova_posicao = self._mov_perseguicao.mover(self._minotauro.obter_posicao_atual(), pos_entrante, percepcao)
            self._minotauro.adicionar_ao_caminho_perseguicao(nova_posicao)
        else:
            nova_posicao = self._mov_normal.mover(self._minotauro.obter_posicao_atual(), pos_entrante, percepcao)
            
        self._minotauro.definir_posicao(nova_posicao)
