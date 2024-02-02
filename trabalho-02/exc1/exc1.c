#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Função para verificar se uma substring do texto coincide com o padrão, considerando o caractere coringa '*'
int verificaString(char* texto, char* padrao, int textoIndex, int padraoIndex) {
    while (padrao[padraoIndex] != '\0' && texto[textoIndex] != '\0') {
        if (padrao[padraoIndex] == '*') {
            // Se o caractere coringa for encontrado, recursivamente tentamos encontrar uma correspondência
            // com o restante do padrão e texto
            while (padrao[padraoIndex] == '*') {
                padraoIndex++;
            }

            // Verificando as correspondências com o restante do padrão e texto
            while (texto[textoIndex] != '\0' && texto[textoIndex] != padrao[padraoIndex]) {
                textoIndex++;
            }
        } else if (texto[textoIndex] != padrao[padraoIndex]) {
            return 0; // Se os caracteres não coincidirem, retorna 0 (sem correspondência)
        }

        textoIndex++;
        padraoIndex++;
    }

    return (padrao[padraoIndex] == '\0'); // Retorna 1 se atingir o final do padrão (correspondência completa)
}

// Função principal para encontrar o padrão no texto com o caractere coringa
void buscaPadrao(char* texto, char* padrao) {
    int n = strlen(texto);
    int m = strlen(padrao);

    for (int i = 0; i <= n - m; i++) {
        if (verificaString(texto, padrao, i, 0)) {
            printf("Padrao encontrado na posicao %d\n", i);
        }
    }
}

int main() {
    char texto[] = "ABABCABABABCABAABABCAB";
    char padrao[] = "A*A*A";

    printf("Procurando pelo padrao com caractere coringa: %s\n", padrao);
    buscaPadrao(texto, padrao);

    return 0;
}
