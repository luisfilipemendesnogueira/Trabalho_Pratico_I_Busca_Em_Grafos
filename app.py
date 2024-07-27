import time

def ler_aquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        labirinto = [list(lista.strip()) for lista in arquivo]
    return labirinto

def encontrar_inicio_e_saida(labirinto):
    inicio = saida = None
    for linha, lista in enumerate(labirinto):
        for coluna, celula in enumerate(lista):
            if celula == 'S':
                inicio = (linha, coluna)
            elif celula == 'E':
                saida = (linha, coluna)
    return inicio, saida

def imprimir_labirinto(labirinto):
    for lista in labirinto:
        print(''.join(lista))

def busca_em_largura(labirinto, inicio, saida):
    from collections import deque
    start_time = time.perf_counter()
    fila = deque([inicio])
    visitados = set()
    veio_de = {}
    visitados.add(inicio)
    while fila:
        atual = fila.popleft()
        if atual == saida:
            break
        for vizinho in obter_vizinhos(labirinto, atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
                veio_de[vizinho] = atual
    caminho = reconstruir_caminho(veio_de, inicio, saida)
    tempo = time.perf_counter() - start_time
    print("\nCaminho da busca em largura:")
    print(" -> ".join(f"({linha},{coluna})" for linha, coluna in caminho))
    print(f"Tempo da busca em largura: {tempo:.6f} s")
    return caminho

def busca_em_profundidade(labirinto, inicio, saida):
    start_time = time.perf_counter()
    pilha = [inicio]
    visitados = set()
    veio_de = {}
    visitados.add(inicio)
    while pilha:
        atual = pilha.pop()
        if atual == saida:
            break
        for vizinho in obter_vizinhos(labirinto, atual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                pilha.append(vizinho)
                veio_de[vizinho] = atual
    caminho = reconstruir_caminho(veio_de, inicio, saida)
    tempo = time.perf_counter() - start_time
    print("\nCaminho da busca em profundidade:")
    print(" -> ".join(f"({linha},{coluna})" for linha, coluna in caminho))
    print(f"Tempo da busca em profundidade: {tempo:.6f} s")
    return caminho

def obter_vizinhos(labirinto, posicao):
    linhas, colunas = len(labirinto), len(labirinto[0])
    linha, coluna = posicao
    vizinhos = []
    for nova_linha, nova_coluna in [(linha-1, coluna), (linha+1, coluna), (linha, coluna-1), (linha, coluna+1)]:
        if 0 <= nova_linha < linhas and 0 <= nova_coluna < colunas and labirinto[nova_linha][nova_coluna] != '#':
            vizinhos.append((nova_linha, nova_coluna))
    return vizinhos

def reconstruir_caminho(veio_de, inicio, saida):
    caminho = []
    atual = saida
    while atual != inicio:
        caminho.append(atual)
        atual = veio_de.get(atual, inicio)
    caminho.append(inicio)
    caminho.reverse()
    return caminho

def main():
    while True:
        nome_arquivo = input("Informe o arquivo (0 para sair): ")
        if nome_arquivo == '0':
            break
        try:
            labirinto = ler_aquivo(nome_arquivo)
            inicio, saida = encontrar_inicio_e_saida(labirinto)
            if not inicio or not saida:
                print("Ponto de início ou saída não encontrado.")
                continue

            print("Labirinto:")
            imprimir_labirinto(labirinto)

            busca_em_largura(labirinto, inicio, saida)
            busca_em_profundidade(labirinto, inicio, saida)

        except FileNotFoundError:
            print("Arquivo não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()