class LeitorArquivo:
    
    def __init__(self, caminho_arquivo):
        self._caminho_arquivo = caminho_arquivo
    
    def ler(self):
        with open(self._caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        return self.processar_linhas(linhas)
    
    def processar_linhas(self, linhas):
        linha_atual = 0
        
        numero_vertices = int(linhas[linha_atual].strip())
        linha_atual += 1
        
        numero_arestas = int(linhas[linha_atual].strip())
        linha_atual += 1
        
        arestas = []
        for i in range(numero_arestas):
            partes = linhas[linha_atual].strip().split()
            origem = int(partes[0])
            destino = int(partes[1])
            peso = float(partes[2])
            arestas.append((origem, destino, peso))
            linha_atual += 1
        
        vertice_entrada = int(linhas[linha_atual].strip())
        linha_atual += 1
        
        vertice_saida = int(linhas[linha_atual].strip())
        linha_atual += 1
        
        posicao_minotauro = int(linhas[linha_atual].strip())
        linha_atual += 1
        
        parametro_percepcao = float(linhas[linha_atual].strip())
        linha_atual += 1
        
        tempo_maximo = float(linhas[linha_atual].strip())
        
        return {
            'numero_vertices': numero_vertices,
            'numero_arestas': numero_arestas,
            'arestas': arestas,
            'vertice_entrada': vertice_entrada,
            'vertice_saida': vertice_saida,
            'posicao_minotauro': posicao_minotauro,
            'parametro_percepcao': parametro_percepcao,
            'tempo_maximo': tempo_maximo
        }
