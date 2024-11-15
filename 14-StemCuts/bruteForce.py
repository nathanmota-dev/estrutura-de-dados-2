def corte_hastes_forca_bruta(T, pedidos):
    if T == 0:
        return 0

    max_valor = 0
    for comprimento, valor in pedidos:
        if T >= comprimento:
            max_valor = max(max_valor, valor + corte_hastes_forca_bruta(T - comprimento, pedidos))
    
    return max_valor

N, T = map(int, input().split())
pedidos = [tuple(map(int, input().split())) for _ in range(N)]

print(corte_hastes_forca_bruta(T, pedidos))
