from Entrante.Entrante import Entrante
from Configuracao.LeitorArquivo import LeitorArquivo
from Labirinto.ConstrutorLabirinto import ConstrutorLabirinto
from Minotauro.Minotauro import Minotauro
from Minotauro.ControladorMinotauro import ControladorMinotauro
import os

class AplicacaoLabirinto:
    
    def __init__(self, caminho_arquivo):
        self._caminho_arquivo = caminho_arquivo
    
    def executar(self):
        dados = self.ler_entrada()
        labirinto = self.construir_labirinto(dados)
        self.exibir_informacoes(labirinto)

        return labirinto
    
    def ler_entrada(self):
        leitor = LeitorArquivo(self._caminho_arquivo)

        return leitor.ler()
    
    def construir_labirinto(self, dados):
        construtor = ConstrutorLabirinto(dados)

        return construtor.construir()
    
    def exibir_informacoes(self, labirinto):
        grafo = labirinto.obter_grafo()
        config = labirinto.obter_configuracao()
        
        print("=" * 60)
        print("LABIRINTO DO MINOTAURO - INFORMAÇÕES CARREGADAS")
        print("=" * 60)
        print(f"Número de vértices: {grafo.obter_numero_vertices()}")
        print(f"Vértice de entrada: {config.obter_vertice_entrada()}")
        print(f"Vértice de saída: {config.obter_vertice_saida()}")
        print(f"Posição inicial do Minotauro: {config.obter_posicao_minotauro()}")
        print(f"Parâmetro de percepção (p): {config.obter_parametro_percepcao()}")
        print(f"Tempo máximo (τ): {config.obter_tempo_maximo()}")
        print("=" * 60)


if __name__ == "__main__":
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_entrada = os.path.join(diretorio_atual, 'entrada.txt')
    app = AplicacaoLabirinto(caminho_entrada)
    labirinto = app.executar()
    config = labirinto.obter_configuracao()
    saida = config.obter_vertice_saida()
    tempo_maximo = config.obter_tempo_maximo()
    percepcao_minotauro = config.obter_parametro_percepcao()

    print("\n" + "=" * 60)
    print("INICIANDO SIMULAÇÃO")
    print("=" * 60)

    entrante = Entrante(config.obter_vertice_entrada(), labirinto.obter_grafo())
    minotauro = Minotauro(config.obter_posicao_minotauro(), labirinto.obter_grafo())
    controlador_minotauro = ControladorMinotauro(minotauro, labirinto.obter_grafo())
    
    momento_captura = None
    while not entrante.verificar_encontrou_saida(saida) and not entrante.verificar_tempo_esgotado(tempo_maximo):
        posicao_anterior_entrante = entrante.obter_posicao_atual()
        entrante.mover_para_proximo_vertice()
        posicao_atual_entrante = entrante.obter_posicao_atual()
        
        tempo_atual = entrante.obter_contador_movimentos().obter_valor()
        tempo_restante = tempo_maximo - tempo_atual

        print(f"Entrante: {posicao_anterior_entrante} -> {posicao_atual_entrante} | Tempo restante: {int(tempo_restante)}")

        posicao_anterior_minotauro = minotauro.obter_posicao_atual()
        controlador_minotauro.mover(posicao_atual_entrante, percepcao_minotauro, tempo_atual)
        posicao_atual_minotauro = minotauro.obter_posicao_atual()
        perseguindo_str = "Sim" if minotauro.esta_perseguindo() else "Não"

        print(f"Minotauro: {posicao_anterior_minotauro} -> {posicao_atual_minotauro} | Perseguindo: {perseguindo_str}")
        print("-" * 60)

        if posicao_atual_entrante == posicao_atual_minotauro and posicao_atual_entrante != saida:
            momento_captura = tempo_atual
            print(f"\nFALHA: O Minotauro capturou o entrante no momento {momento_captura}!")
            break

        if posicao_atual_entrante == saida:
            print(f"\nSUCESSO: O entrante encontrou a saída no momento {tempo_atual}!")
            break

    print("=" * 60)
    print("RELATÓRIO DA SIMULAÇÃO")
    print("=" * 60)

    tempo_final = entrante.obter_contador_movimentos().obter_valor()
    tempo_restante_final = tempo_maximo - tempo_final

    if entrante.verificar_encontrou_saida(saida):
        print("Resultado: SUCESSO! O entrante encontrou a saída.")
    elif entrante.verificar_tempo_esgotado(tempo_maximo):
        print("Resultado: FALHA. O tempo máximo foi esgotado.")
    elif momento_captura is not None:
        print("Resultado: FALHA. O entrante foi capturado pelo Minotauro.")
    else:
        print("Resultado: FALHA. Motivo desconhecido.")

    print(f"Tempo total gasto: {tempo_final}")
    print(f"Tempo restante: {int(tempo_restante_final)}")
    
    print("\n--- Estatísticas do Entrante ---")
    print(f"Sequência de vértices visitados: {entrante.obter_sequencia_visitados()}")
    
    print("\n--- Atividade do Minotauro ---")
    
    momento_deteccao = controlador_minotauro.obter_momento_deteccao()
    if momento_deteccao is not None:
        print(f"Momento da detecção: {momento_deteccao}")
        if momento_captura is not None:
            print(f"Momento da captura: {momento_captura}")
        caminho_perseguicao = minotauro.obter_caminho_perseguicao()
        if caminho_perseguicao:
            print(f"Caminho de perseguição: {caminho_perseguicao}")
    else:
        print("O Minotauro não detectou o entrante.")

    print("\n--- Posições Finais ---")
    print(f"Posição final do Entrante: {entrante.obter_posicao_atual()}")
    print(f"Posição final do Minotauro: {minotauro.obter_posicao_atual()}")
    print("=" * 60)
