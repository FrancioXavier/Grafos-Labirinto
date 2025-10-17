# Grafos — Labirinto de Creta

Simulação do Labirinto de Creta modelada em grafos. O projeto inclui:

- **Regras de Deslocamento:** Movimentação do prisioneiro dentro do labirinto.
- **Perseguição do Minotauro:** Implementação da perseguição do Minotauro ao prisioneiro.
- **Registro de Caminho:** Armazenamento do trajeto percorrido pelo prisioneiro.
- **Estratégia do "Novelo de Lã":** Lógica para evitar ciclos e orientar a fuga, baseada no mito de Teseu.

## Execução

O motor de simulação principal pode ser executado através do arquivo `main.py`.

## Recursos

- **Estratégias de Movimento Modulares:** Diferentes estratégias de movimentação podem ser implementadas e testadas.
- **Relatório de Execução:** Geração de um relatório com os resultados da simulação.

## Sumário

- Visão Geral
- Arquitetura e Classes
- Como Executar
- Entrada e Saída
- Decisões de Projeto
- Testes e Casos de Borda

## Visão Geral

O sistema carrega uma instância de grafo e os parâmetros do problema (posições iniciais, percepção, etc.), executa a simulação em turnos alternados entre o prisioneiro e o Minotauro, e aplica as lógicas de percepção e os modos de perseguição. O resultado de cada simulação (fuga ou captura) é registrado, e o caminho percorrido por cada entidade é salvo para auditoria e análise posterior.

## Arquitetura e Classes

### `CaminhoPercorrido.py`
Essa classe registra e expõe o caminho percorrido ao longo da simulação. Manter o histórico separado simplifica a auditoria, visualização e testes, sem acoplar o motor de simulação ao formato de log.

- **Responsabilidades:** Armazenar a sequência de vértices/estados, adicionar passos a cada rodada e fornecer consultas como "último passo" e "trajetória completa".
- **Métodos esperados:** `adicionar_passo(vertice)`, `ultimo()`, `como_lista()`.

### `Movimentacao.py` (Interface/Base)
Define um contrato abstrato para as estratégias de movimento. Como a política de deslocamento muda (de "normal" para "perseguição"), uma interface comum permite trocá-las dinamicamente sem alterar o restante do sistema.

- **Responsabilidades:** Declarar a assinatura do método `proximo_passo` e quaisquer hooks de configuração necessários. Não implementa a lógica concreta.

### `MovimentacaoNormal.py`
Implementa a movimentação padrão do Minotauro quando não está em perseguição ativa. Fora do alcance do prisioneiro, sua política é de patrulha ou exploração com critérios locais simples.

- **Responsabilidades:** Escolher o próximo vértice seguindo a heurística padrão, evitar movimentos inválidos e respeitar o limite de 1 passo por rodada.
- **Destaques:** Utiliza a vizinhança do vértice atual e pode incluir desempate determinístico para evitar oscilações.

### `MovimentacaoPerseguicao.py`
Implementa a movimentação de perseguição. As regras mudam quando o Minotauro detecta o prisioneiro, permitindo acelerar (2 passos) ou seguir o caminho mínimo para interceptá-lo.

- **Responsabilidades:** Calcular o próximo passo para reduzir a distância até o alvo, potencialmente consumindo dois movimentos por turno.
- **Integração:** É ativada e desativada pelo `ControladorMinotauro` com base na percepção `p(G)`.

### `ControladorMinotauro.py`
Coordena o estado e o modo de deslocamento do Minotauro (normal vs. perseguição). Centralizar a decisão reduz o acoplamento e concentra as regras de transição entre os modos.

- **Responsabilidades:** Decidir quando alternar para o modo de perseguição, delegar a chamada para a estratégia de movimento correta e manter o estado interno (posição, alvo, etc.).
- **Interações:** Consome as classes `MovimentacaoNormal` e `MovimentacaoPerseguicao`, consulta a percepção e atualiza a posição do Minotauro.

### `Minotauro.py`
Modela a entidade Minotauro, separando seu estado e operações da lógica de controle.

- **Responsabilidades:** Armazenar a posição atual, aplicar o movimento (`mover_para(vertice)`) e registrar eventos como detecção e colisão com o prisioneiro.

### `NoveloLa.py`
Implementa a estratégia do “novelo de lã” para o prisioneiro. O uso da memória de nós visitados evita ciclos e ajuda a explorar o labirinto ou retroceder com segurança.

- **Responsabilidades:** Manter uma pilha de marcações, decidir o próximo movimento para minimizar revisitas e permitir *backtracking* quando encurralado.
- **Efeitos:** Melhora a cobertura do grafo e aumenta a chance de fuga dentro do tempo limite `τ(G)`.

### `main.py`
Ponto de entrada da aplicação. Orquestra a simulação do início ao fim, incluindo o parsing de argumentos, a criação de entidades, o laço de rodadas e a emissão dos resultados.

- **Responsabilidades:** Configurar a semente aleatória, carregar o grafo, instanciar prisioneiro e Minotauro, executar a simulação até uma condição de término (fuga, captura ou tempo limite) e gerar o relatório final.

### `__init__.py`
Arquivos vazios que definem os diretórios como pacotes Python, permitindo imports relativos claros e facilitando a distribuição e os testes do projeto.

## Como Executar

### Requisitos
- Python 3.10+

### Passos
1. Clone o repositório e acesse a pasta raiz do projeto.
2. Execute o script principal com os argumentos desejados:
   python src/main.py --input data/instancia.txt --seed 42 --p 3 --tau 100 --verbose
   A saída será um relatório no console (e/ou arquivo), indicando o resultado (FUGA/MORTE), o tempo total e as trajetórias.

### Flags Sugeridas

-   `--input`: Caminho do arquivo da instância (grafo e parâmetros).
-   `--seed`: Semente para garantir a reprodutibilidade de elementos aleatórios.
-   `--p`: Alcance da percepção `p(G)` do Minotauro.
-   `--tau`: Limite de tempo/rodadas `τ(G)` da simulação.
-   `--verbose`: Ativa logs detalhados de cada turno.

## Entrada e Saída

Entrada
O arquivo de instância define o grafo e os parâmetros da simulação.

n m
u1 v1 w1
u2 v2 w2
...
pos_pris pos_mino pos_saida p tau

Saída
Resultado (FUGA/MORTE), tempo total, caminhos tomados, momento da detecção e eventos de perseguição/combate.​

# Testes e Casos de Borda

## Cenários Mínimos
* **Grafo pequeno com caminho direto de fuga:** Validar a trajetória básica do prisioneiro e a corretude do caminho encontrado.

## Perseguição Forçada
* **`p(G)` alto:** Verificar a alternância correta para a estratégia `MovimentacaoPerseguicao` e a execução de passos duplos pelo guarda.

## Tempo Limite
* **`τ(G)` curto:** Conferir se a simulação termina adequadamente por estouro de tempo e se o relatório final reflete esse resultado corretamente.

## Ciclos e Becos
* **Validar `NoveloLa`:** Garantir que o algoritmo evita laços infinitos e consegue retroceder (backtracking) de forma eficaz quando encontra becos sem saída.

## Reprodutibilidade
* **Rodar com `--seed` fixa:** Comparar os caminhos gerados e o resultado final em múltiplas execuções para garantir consistência e determinismo.











