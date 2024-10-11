import heapq

# Grafo representado como um dicionário de adjacência
grafo = {
    'a': {'b': 61, 'd': 42, 'c': 50},
    'b': {'a': 61, 'j': 17, 'd': 32, 'f': 29},
    'c': {'a': 50, 'd': 56, 'e': 67},
    'd': {'a': 42, 'b': 32, 'f': 62, 'g': 85, 'c': 56, 'e': 45},
    'e': {'c': 67, 'd': 45, 'g': 72, 'i': 73},
    'f': {'b': 29, 'j': 30, 'l': 45, 'd': 62, 'g': 20},
    'g': {'d': 85, 'f': 20, 'l': 35, 'h': 40, 'e': 72, 'i': 60},
    'h': {'g': 40, 'l': 50, 'm': 21},
    'i': {'e': 73, 'g': 60, 'm': 50},
    'j': {'b': 17, 'f': 30, 'l': 30},
    'l': {'j': 30, 'f': 45, 'g': 35, 'h': 50},
    'm': {'h': 21, 'i': 50}
}

# Algoritmo de Dijkstra
def dijkstra(grafo, inicio, fim):
    # Inicializando distâncias e fila de prioridade
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

        # Condição de parada se chegarmos ao destino
        if vertice_atual == fim:
            break

        # Se a distância atual é maior do que a já registrada, ignora
        if distancia_atual > distancias[vertice_atual]:
            continue

        # Verificar vizinhos e atualizar distâncias
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = distancia_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    return distancias[fim]

# Executando o algoritmo de Dijkstra para o grafo dado, de 'a' até 'm'
menor_distancia = dijkstra(grafo, 'a', 'm')
print(f"A menor distancia de 'a' ate 'm' eh: {menor_distancia}")
