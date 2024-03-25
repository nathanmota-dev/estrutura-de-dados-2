class Vertice:
    def __init__(self, nome, distancia=float('inf')):
        self.nome = nome
        self.antecessor = self
        self.distancia = distancia
        self.adjacentes = {}
        self.caminhoMaisCurto = []

    def adicionarVerticeAdjacente(self, vertice, distancia):
        self.adjacentes[vertice] = distancia


class Caminho:
    def __init__(self, distancia, caminho):
        self.distancia = distancia
        self.caminho = caminho

    def imprimirCaminho(self):
        resultado = "Distancia Total: " + str(self.distancia) + " - Caminho: "
        caracteres_caminho = list(self.caminho)

        for char in reversed(caracteres_caminho):
            resultado += char + " "

        print(resultado)


def encontrarCaminhoMaisCurto(vertices, inicial, final):
    atual = final

    for vertice in vertices:
        for chave, valor in vertice.adjacentes.items():
            distancia_entre_vertices = vertice.adjacentes[chave]
            distancia_final = vertice.distancia + distancia_entre_vertices

            if distancia_final < chave.distancia:
                chave.antecessor = vertice
                chave.distancia = distancia_final

    for vertice in vertices:
        print(vertice.nome + ": " + vertice.antecessor.nome + " - " + str(vertice.distancia))

    caminho_mais_curto_final = Caminho(0, "")
    caminho_mais_curto_final.caminho += atual.nome

    while atual != inicial and atual.distancia < float('inf'):
        caminho_mais_curto_final.distancia += atual.distancia
        atual = atual.antecessor
        caminho_mais_curto_final.caminho += atual.nome

    return caminho_mais_curto_final


if __name__ == "__main__":
    vertices = []
    A = Vertice('A', 0)
    B = Vertice('B')
    C = Vertice('C')
    D = Vertice('D')
    E = Vertice('E')
    F = Vertice('F')

    A.adicionarVerticeAdjacente(B, 2)
    A.adicionarVerticeAdjacente(C, 4)

    B.adicionarVerticeAdjacente(C, 3)
    B.adicionarVerticeAdjacente(D, 1)
    B.adicionarVerticeAdjacente(E, 5)

    C.adicionarVerticeAdjacente(D, 2)

    D.adicionarVerticeAdjacente(E, 1)
    D.adicionarVerticeAdjacente(F, 4)

    E.adicionarVerticeAdjacente(F, 2)

    vertices.extend([A, B, C, D, E, F])

    caminho_mais_curto = encontrarCaminhoMaisCurto(vertices, A, D)
    caminho_mais_curto.imprimirCaminho()
