class No:
    def __init__(self, caractere, frequencia):
        self.caractere = caractere
        self.frequencia = frequencia
        self.esquerda = None
        self.direita = None

def calcula_frequencias(texto):
    frequencias = {}
    for caractere in texto:
        if caractere in frequencias:
            frequencias[caractere] += 1
        else:
            frequencias[caractere] = 1
    return frequencias

def constroi_arvore(frequencias):
    fila = [No(caractere, frequencia) for caractere, frequencia in frequencias.items()]
    while len(fila) > 1:
        fila = sorted(fila, key=lambda no: no.frequencia)
        esquerda = fila.pop(0)
        direita = fila.pop(0)
        pai = No(None, esquerda.frequencia + direita.frequencia)
        pai.esquerda = esquerda
        pai.direita = direita
        fila.append(pai)
    return fila[0]

def codifica_arvore(arvore, codigo='', codigos={}):
    if arvore.caractere:
        codigos[arvore.caractere] = codigo
    else:
        codifica_arvore(arvore.esquerda, codigo + '0', codigos)
        codifica_arvore(arvore.direita, codigo + '1', codigos)
    return codigos

def codifica_texto(texto, codigos):
    texto_codificado = ''
    for caractere in texto:
        texto_codificado += codigos[caractere]
    return texto_codificado

def decodifica_texto(texto_codificado, arvore):
    texto_decodificado = ''
    no_atual = arvore
    for bit in texto_codificado:
        if bit == '0':
            no_atual = no_atual.esquerda
        else:
            no_atual = no_atual.direita
        if no_atual.caractere:
            texto_decodificado += no_atual.caractere
            no_atual = arvore
    return texto_decodificado

def comprime(texto):
    frequencias = calcula_frequencias(texto)
    arvore = constroi_arvore(frequencias)
    codigos = codifica_arvore(arvore)
    texto_codificado = codifica_texto(texto, codigos)
    return texto_codificado, arvore

def descomprime(texto_codificado, arvore):
    return decodifica_texto(texto_codificado, arvore)

texto = "Este é um exemplo de texto para compressão usando o algoritmo de Huffman"
texto_codificado, arvore = comprime(texto)
print("Texto codificado:", texto_codificado)
texto_decodificado = descomprime(texto_codificado, arvore)
print("Texto decodificado:", texto_decodificado)








