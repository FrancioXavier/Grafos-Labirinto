from Grafos.Grafo import Grafo

class Minotauro:
    def __init__(self, posicao_inicial: int, grafo: Grafo):
        self._posicao_atual = posicao_inicial
        self._grafo = grafo
        self._perseguindo = False
        self._caminho_perseguicao = []
        self._distancias = grafo.floyd_warshall()

    def obter_posicao_atual(self) -> int:
        return self._posicao_atual

    def definir_posicao(self, nova_posicao: int):
        self._posicao_atual = nova_posicao

    def esta_perseguindo(self) -> bool:
        return self._perseguindo

    def iniciar_perseguicao(self):
        self._perseguindo = True

    def parar_perseguicao(self):
        self._perseguindo = False

    def obter_caminho_perseguicao(self):
        return self._caminho_perseguicao

    def adicionar_ao_caminho_perseguicao(self, vertice: int):
        self._caminho_perseguicao.append(vertice)

    def limpar_caminho_perseguicao(self):
        self._caminho_perseguicao = []
