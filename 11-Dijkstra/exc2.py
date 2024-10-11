import heapq

# Grafo representado como um dicionário
grafo = {
    'O': {'R': 4, 'K': 1},
    'K': {'O': 1, 'R': 2, 'G': 1},
    'R': {'O': 4, 'K': 2, 'E': 0, 'G': 0},
    'E': {'R': 0, 'G': 3, 'A': 2},
    'G': {'K': 1, 'R': 0, 'E': 3, 'A': 1, 'Q': 5},
    'A': {'E': 2, 'G': 1, 'Q': 4, 'T': 3, 'D': 3},
    'Q': {'G': 5, 'A': 4, 'M': 2},
    'T': {'A': 3, 'M': 2, 'D': 4, 'X': 2},
    'M': {'Q': 2, 'T': 2},
    'D': {'A': 3, 'T': 4, 'X': 3},
    'X': {'T': 2, 'D': 3}
}

# Função do algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[inicio] = 0
    precedencia = {vertice: None for vertice in grafo}
    fila_prioridade = [(0, inicio)]

    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        if distancia_atual > distancias[vertice_atual]:
            continue

        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                precedencia[vizinho] = vertice_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))

    return distancias, precedencia

# Função para reconstruir o caminho a partir da tabela de precedência
def encontrar_caminho(precedencia, inicio, fim):
    caminho = []
    atual = fim
    while atual:
        caminho.append(atual)
        atual = precedencia[atual]
    caminho.reverse()
    return caminho

# Execução do algoritmo de Dijkstra partindo de G
distancias, precedencia = dijkstra(grafo, 'G')

# Exibe a tabela de distâncias e precedência final
print("Tabela de Distancias:")
for vertice in distancias:
    print(f"{vertice}: {distancias[vertice]}")

print("\nTabela de Precedencias:")
for vertice in precedencia:
    print(f"{vertice}: {precedencia[vertice]}")

# Exibe o caminho para o paciente T
caminho_para_T = encontrar_caminho(precedencia, 'G', 'T')
print(f"\nCaminho da area G ate o paciente T: {' -> '.join(caminho_para_T)}")
