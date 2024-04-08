def busca_em_largura(grafo, emparelhamento, distancias):
    infinito = float("inf") 
    fila_inicio = 0
    fila_fim = 0
    fila = [0] * len(distancias)  # Preparando uma fila com tamanho máximo possível

    for u in range(1, len(distancias)):
        if emparelhamento[u] == 0:
            distancias[u] = 0
            fila[fila_fim] = u  # Adiciona na fila
            fila_fim += 1
        else:
            distancias[u] = infinito

    distancias[0] = infinito

    while fila_inicio < fila_fim:
        u = fila[fila_inicio]
        fila_inicio += 1  # Remove da fila

        if u != 0:
            for v in grafo[u]:
                if distancias[emparelhamento[v]] == infinito:
                    distancias[emparelhamento[v]] = distancias[u] + 1
                    fila[fila_fim] = emparelhamento[v]  # Adiciona na fila
                    fila_fim += 1

    return distancias[0] != infinito


def busca_em_profundidade(grafo, emparelhamento, distancias, u):
    if u != 0:
        for v in grafo[u]:
            if distancias[emparelhamento[v]] == distancias[
                u
            ] + 1 and busca_em_profundidade(
                grafo, emparelhamento, distancias, emparelhamento[v]
            ):
                emparelhamento[u] = v
                emparelhamento[v] = u
                return True
        distancias[u] = float("inf")
        return False
    return True


def hopcroft_karp(grafo):
    emparelhamento = [0] * (len(grafo) + 1)
    distancias = [0] * (len(grafo) + 1)
    emparelhamentos_totais = 0

    while busca_em_largura(grafo, emparelhamento, distancias):
        for u in range(1, len(grafo)):
            if emparelhamento[u] == 0 and busca_em_profundidade(
                grafo, emparelhamento, distancias, u
            ):
                emparelhamentos_totais += 1

    return emparelhamentos_totais, emparelhamento


# Exemplo de uso
grafo = {1: [4, 5], 2: [5], 3: [6], 4: [], 5: [], 6: []}

# Chamada da função e impressão dos resultados
emparelhamentos_totais, emparelhamento = hopcroft_karp(grafo)
print(f"Número total de emparelhamentos: {emparelhamentos_totais}")
print(f"Emparelhamentos: {emparelhamento}")
