from .ListaAdjacencias import ListaAdjacencias
from .Aresta import Aresta
import heapq

class Grafo:
    
    def __init__(self, numero_vertices):
        self._numero_vertices = numero_vertices
        self._adjacencias = self.inicializar_adjacencias()
    
    def inicializar_adjacencias(self):
        adjacencias = {}
        for vertice in range(self._numero_vertices):
            adjacencias[vertice] = ListaAdjacencias()

        return adjacencias
    
    def adicionar_aresta(self, origem, destino, peso):
        self.validar_vertice(origem)
        self.validar_vertice(destino)
        
        aresta_ida = Aresta(destino, peso)
        aresta_volta = Aresta(origem, peso)
        
        self._adjacencias[origem].adicionar(aresta_ida)
        self._adjacencias[destino].adicionar(aresta_volta)
    
    def obter_adjacentes(self, vertice):
        self.validar_vertice(vertice)

        return self._adjacencias[vertice].obter_todas()
    
    def existe_aresta(self, origem, destino):
        self.validar_vertice(origem)
        self.validar_vertice(destino)

        return self._adjacencias[origem].existe_adjacencia_para(destino)
    
    def obter_peso_aresta(self, origem, destino):
        self.validar_vertice(origem)
        self.validar_vertice(destino)

        return self._adjacencias[origem].obter_peso_para(destino)
    
    def obter_numero_vertices(self):
        return self._numero_vertices
    

    def floyd_warshall(self):
        distancias = [[float('infinity')] * self._numero_vertices for _ in range(self._numero_vertices)]
        
        for vertice in range(self._numero_vertices):
            distancias[vertice][vertice] = 0
        
        for origem in range(self._numero_vertices):
            for aresta in self.obter_adjacentes(origem):
                destino = aresta.obter_destino()
                peso = aresta.obter_peso()
                distancias[origem][destino] = peso
        
        for k in range(self._numero_vertices):
            for i in range(self._numero_vertices):
                for j in range(self._numero_vertices):
                    if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                        distancias[i][j] = distancias[i][k] + distancias[k][j]
        
        return distancias
    
    def dijkstra(self, inicio):
        distancias = {vertice: float('infinity') for vertice in range(self._numero_vertices)}
        distancias[inicio] = 0
        caminho = {}

        pq = [(0, inicio)]

        while len(pq) > 0:
            distancia_atual, vertice_atual = heapq.heappop(pq)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for aresta in self.obter_adjacentes(vertice_atual):
                vizinho = aresta.obter_destino()
                peso = aresta.obter_peso()
                distancia = distancia_atual + peso

                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    caminho[vizinho] = vertice_atual
                    heapq.heappush(pq, (distancia, vizinho))
        
        return distancias, caminho

    def obter_caminho_minimo(self, inicio, fim):
        _distancias, predecessores = self.dijkstra(inicio)
        caminho = []
        atual = fim
        
        if fim not in predecessores and inicio != fim:
            return []

        while atual in predecessores:
            caminho.insert(0, atual)
            atual = predecessores[atual]
        
        if atual == inicio:
            caminho.insert(0, inicio)
        
        return caminho

    def validar_vertice(self, vertice):
        if vertice < 0 or vertice >= self._numero_vertices:
            raise ValueError(f"Vértice {vertice} inválido. Deve estar entre 0 e {self._numero_vertices - 1}")