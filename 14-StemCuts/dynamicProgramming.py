def corte_hastes(N, T, pedidos):
    dp = [0] * (T + 1)
    
    for t in range(1, T + 1):
        for i in range(N):
            comprimento, valor = pedidos[i]
            if t >= comprimento:
                dp[t] = max(dp[t], dp[t - comprimento] + valor)
    return dp[T]

N, T = map(int, input().split())
pedidos = [tuple(map(int, input().split())) for _ in range(N)]

print(corte_hastes(N, T, pedidos))
