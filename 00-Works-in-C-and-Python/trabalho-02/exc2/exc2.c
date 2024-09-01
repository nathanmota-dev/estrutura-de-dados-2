#include <stdio.h>
#include <string.h>

#define d 256  // Tamanho do conjunto de caracteres (ASCII)

void buscaMultiPadroes(char padroes[][50], int numPadroes, char texto[], int q) {
    int N = strlen(texto);
    int h = 1;

    for (int p = 0; p < numPadroes; p++) {
        char *padrao = padroes[p];
        int M = strlen(padrao);
        int i, j;
        int pHash = 0;  // Hash do padrão
        int tHash = 0;  // Hash da janela deslizante no texto

        // Valor de h para o hash do padrão e do texto
        for (i = 0; i < M - 1; i++)
            h = (h * d) % q;

        // Calcula o hash do padrão e da primeira janela no texto
        for (i = 0; i < M; i++) {
            pHash = (d * pHash + padrao[i]) % q;
            tHash = (d * tHash + texto[i]) % q;
        }

        // Desliza a janela sobre o texto
        for (i = 0; i <= N - M; i++) {
            // Verifica se o hash do padrão e da janela deslizante são iguais
            if (pHash == tHash) {
                // Verifica caractere por caractere para evitar colisões de hash
                for (j = 0; j < M; j++) {
                    if (texto[i + j] != padrao[j])
                        break;
                }
                if (j == M)
                    printf("Padrao #%d encontrado na posicao %d\n", p + 1, i);
            }

            // Calcula o hash para a próxima janela no texto
            if (i < N - M) {
                tHash = (d * (tHash - texto[i] * h) + texto[i + M]) % q;

                // Garante que o hash seja não-negativo
                if (tHash < 0)
                    tHash = (tHash + q);
            }
        }
    }
}

int main() {
    char texto[] = "AABCAAADAABCAADAABCAA";
    char padroes[][50] = {"AABC", "ADA", "CAADA"};
    int numPadroes = sizeof(padroes) / sizeof(padroes[0]);
    int q = 101;  // Um número primo para reduzir as colisões de hash

    buscaMultiPadroes(padroes, numPadroes, texto, q);

    return 0;
}