#include <stdio.h>
#include <stdlib.h>

// Estrutura para representar uma aresta no grafo
struct Aresta
{
    int origem, destino, peso;
};

// Estrutura para representar um grafo
struct Grafo
{
    int V, E;              // V = Número de vértices, E = Número de arestas
    struct Aresta *aresta; // Lista de todas as arestas
};

// Estrutura para representar subconjuntos para union-find (união e busca)
struct subset
{
    int pai;
    int rank;
};

// Função para criar um grafo com V vértices e E arestas
struct Grafo *criarGrafo(int V, int E)
{
    struct Grafo *grafo = (struct Grafo *)malloc(sizeof(struct Grafo));
    grafo->V = V;
    grafo->E = E;
    grafo->aresta = (struct Aresta *)malloc(grafo->E * sizeof(struct Aresta));
    return grafo;
}

// Função para encontrar o conjunto de um elemento i
int encontrar(struct subset subsets[], int i)
{
    if (subsets[i].pai != i)
        subsets[i].pai = encontrar(subsets, subsets[i].pai);
    return subsets[i].pai;
}

// Função para unir dois subconjuntos em um único subconjunto
void unir(struct subset subsets[], int x, int y)
{
    int xraiz = encontrar(subsets, x);
    int yraiz = encontrar(subsets, y);

    if (subsets[xraiz].rank < subsets[yraiz].rank)
        subsets[xraiz].pai = yraiz;
    else if (subsets[xraiz].rank > subsets[yraiz].rank)
        subsets[yraiz].pai = xraiz;
    else
    {
        subsets[yraiz].pai = xraiz;
        subsets[xraiz].rank++;
    }
}

// Construir a Árvore Geradora Mínima
void boruvkaMST(struct Grafo *grafo)
{
    int V = grafo->V, E = grafo->E;
    struct Aresta *aresta = grafo->aresta;
    struct subset *subsets = (struct subset *)malloc(V * sizeof(struct subset));
    int *arestasMaisBaratas = (int *)malloc(V * sizeof(int));

    // Inicializar subconjuntos e arestasMaisBaratas
    for (int v = 0; v < V; ++v)
    {
        subsets[v].pai = v;
        subsets[v].rank = 0;
        arestasMaisBaratas[v] = -1;
    }

    int numComponentes = V;
    int pesoMST = 0;

    // Continuar até que o grafo se torne uma única componente conectada
    while (numComponentes > 1)
    {
        // Para cada vértice, encontrar a aresta mais barata que conecta a outra componente
        for (int i = 0; i < E; i++)
        {
            int conjunto1 = encontrar(subsets, aresta[i].origem);
            int conjunto2 = encontrar(subsets, aresta[i].destino);

            if (conjunto1 != conjunto2)
            {
                if (arestasMaisBaratas[conjunto1] == -1 ||
                    aresta[arestasMaisBaratas[conjunto1]].peso > aresta[i].peso)
                    arestasMaisBaratas[conjunto1] = i;

                if (arestasMaisBaratas[conjunto2] == -1 ||
                    aresta[arestasMaisBaratas[conjunto2]].peso > aresta[i].peso)
                    arestasMaisBaratas[conjunto2] = i;
            }
        }

        // Adicionar as arestas mais baratas de cada componente ao resultado
        for (int i = 0; i < V; i++)
        {
            if (arestasMaisBaratas[i] != -1)
            {
                int conjunto1 = encontrar(subsets, aresta[arestasMaisBaratas[i]].origem);
                int conjunto2 = encontrar(subsets, aresta[arestasMaisBaratas[i]].destino);

                if (conjunto1 != conjunto2)
                {
                    printf("Aresta %d-%d com peso %d incluida na MST\n",
                           aresta[arestasMaisBaratas[i]].origem, aresta[arestasMaisBaratas[i]].destino,
                           aresta[arestasMaisBaratas[i]].peso);
                    pesoMST += aresta[arestasMaisBaratas[i]].peso;
                    unir(subsets, conjunto1, conjunto2);
                    numComponentes--;
                }
            }
        }
    }

    printf("Peso da MST e %d\n", pesoMST);
    free(subsets);
    free(arestasMaisBaratas);
}

// Função para adicionar uma aresta ao grafo
void adicionarAresta(struct Grafo *grafo, int indice, int origem, int destino, int peso)
{
    grafo->aresta[indice].origem = origem;
    grafo->aresta[indice].destino = destino;
    grafo->aresta[indice].peso = peso;
}

// Programa principal
int main()
{
    int V = 4; // Número de vértices
    int E = 5; // Número de arestas
    struct Grafo *grafo = criarGrafo(V, E);

    // Adicionando arestas
    adicionarAresta(grafo, 0, 0, 1, 10);
    adicionarAresta(grafo, 1, 0, 2, 6);
    adicionarAresta(grafo, 2, 0, 3, 5);
    adicionarAresta(grafo, 3, 1, 3, 15);
    adicionarAresta(grafo, 4, 2, 3, 4);

    printf("Arestas da Arvore Geradora Minima (MST) sao:\n");
    boruvkaMST(grafo);

    return 0;
}
