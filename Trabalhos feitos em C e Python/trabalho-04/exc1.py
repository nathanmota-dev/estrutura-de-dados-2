def imprimir_binario(numero):

  if numero == 0:
    print(0, end="")
  else:
    imprimir_binario(numero // 2)
    print(numero % 2, end="")

numero = 13
imprimir_binario(numero)
