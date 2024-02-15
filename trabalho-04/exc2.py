def busca_binaria(vetor, elemento, inicio, fim):

  if inicio > fim:
    return False

  meio = (inicio + fim) // 2

  if vetor[meio] == elemento:
    return True
  elif vetor[meio] < elemento:
    return busca_binaria(vetor, elemento, meio + 1, fim)
  else:
    return busca_binaria(vetor, elemento, inicio, meio - 1)

vetor = [1, 3, 5, 7, 9, 11, 13, 15]
elemento = 11

presente = busca_binaria(vetor, elemento, 0, len(vetor) - 1)

if presente:
  print("O elemento", elemento, "está presente no vetor.")
else:
  print("O elemento", elemento, "não está presente no vetor.")
