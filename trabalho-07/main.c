#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAXN 100 // Número máximo de vértices no grafo
#define INF INT_MAX // Valor infinito para representar distâncias inexistentes

int fila[MAXN];
int inicioFila = 0, fimFila = 0;
int grafo[MAXN][MAXN] = {0}; 
int emparelhamento[MAXN]; 
int distancias[MAXN]; 
int n; // Número de vértices no grafo

void insereFila(int v) {
    fila[fimFila++] = v;
}

int removeFila() {
    return fila[inicioFila++];
}

int filaVazia() {
    return inicioFila == fimFila;
}

// Busca em largura para encontrar caminhos de aumento
int buscaEmLargura() {
    for (int i = 1; i <= n; i++) {
        if (emparelhamento[i] == 0) {
            distancias[i] = 0;
            insereFila(i);
        } else {
            distancias[i] = INF; // Distâncias infinitas para vértices já emparelhados
        }
    }
    distancias[0] = INF;

    while (!filaVazia()) {
        int u = removeFila();
        if (u != 0) {
            for (int v = 1; v <= n; v++) {
                if (grafo[u][v] && distancias[emparelhamento[v]] == INF) {
                    distancias[emparelhamento[v]] = distancias[u] + 1;
                    insereFila(emparelhamento[v]);
                }
            }
        }
    }

    return distancias[0] != INF;
}

// Busca em profundidade para encontrar e marcar caminhos de aumento
int buscaEmProfundidade(int u) {
    if (u != 0) {
        for (int v = 1; v <= n; v++) {
            if (grafo[u][v] && distancias[emparelhamento[v]] == distancias[u] + 1) {
                if (buscaEmProfundidade(emparelhamento[v])) {
                    emparelhamento[u] = v;
                    emparelhamento[v] = u;
                    return 1;
                }
            }
        }
        distancias[u] = INF; // Marca o vértice como visitado
        return 0;
    }
    return 1;
}

void hopcroftKarp() {
    for (int i = 0; i <= n; i++) {
        emparelhamento[i] = 0; // Inicializa todos os emparelhamentos como 0
    }

    int emparelhamentosTotais = 0;
    while (buscaEmLargura()) {
        for (int u = 1; u <= n; u++) {
            if (emparelhamento[u] == 0 && buscaEmProfundidade(u)) { // Se o vértice não está emparelhado e existe um caminho de aumento
                emparelhamentosTotais++;
            }
        }
    }

    printf("Numero total de emparelhamentos: %d\n", emparelhamentosTotais);
    for (int u = 1; u <= n; u++) {
        if (emparelhamento[u] > 0) {
            printf("%d esta emparelhado com %d\n", u, emparelhamento[u]);
        }
    }
}

int main() {

    // Definindo o número de vértices do grafo bipartido
    n = 6;

    // Inicializando o grafo 
    grafo[1][4] = 1; grafo[4][1] = 1;
    grafo[1][5] = 1; grafo[5][1] = 1;
    grafo[2][5] = 1; grafo[5][2] = 1;
    grafo[3][6] = 1; grafo[6][3] = 1;

    hopcroftKarp();

    return 0;
}