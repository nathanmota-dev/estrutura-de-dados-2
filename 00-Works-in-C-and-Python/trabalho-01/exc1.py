import random

# Gera aleatoriamente 100 números entre 0 e 100
colecao = [random.randint(0, 100) for _ in range(100)]

# Valor a ser procurado
valor_procurado = random.choice(colecao)

def busca_sequencial(valor):
    posicao = -1
    verificações = 0
    ocorrencias = []

    for i, num in enumerate(colecao):  # enumerate retorna o índice e o valor
        verificações += 1
        if num == valor:
            posicao = i
            ocorrencias.append(i)  # append adiciona o valor no final da lista

    return posicao, verificações, ocorrencias


def busca_binaria(valor):
    colecao_ordenada = sorted(colecao)  # sorted retorna uma lista ordenada
    posicao = -1
    verificações = 0
    ocorrencias = []

    inicio = 0
    fim = len(colecao_ordenada) - 1  # len retorna o tamanho da lista

    while inicio <= fim:
        meio = (inicio + fim) // 2  # // retorna a divisão como int
        verificações += 1

        if colecao_ordenada[meio] == valor:
            posicao = colecao.index(valor)
            ocorrencias.append(posicao)
            break
        elif colecao_ordenada[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return posicao, verificações, ocorrencias


# Busca sequencial
posicao_sequencial, verificações_sequencial, ocorrencias_sequencial = busca_sequencial(
    valor_procurado
)

# Busca binária
posicao_binaria, verificações_binaria, ocorrencias_binaria = busca_binaria(
    valor_procurado
)

# Resultados
print(f"Colecao: {colecao}")
print(f"Valor Procurado: {valor_procurado}\n")

# Busca Sequencial
print("Busca Sequencial:")
print(f"Posicao: {posicao_sequencial}")
print(f"Ocorrencias: {ocorrencias_sequencial}")
print(f"Quantidade de Verificacoes: {verificações_sequencial}\n")

# Busca Binária
print("Busca Binaria:")
print(f"Posicao: {posicao_binaria}")
print(f"Ocorrencias: {ocorrencias_binaria}")
print(f"Quantidade de Verificacoes: {verificações_binaria}")
