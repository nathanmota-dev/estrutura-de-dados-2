const d = 256; // Tamanho do conjunto de caracteres (ASCII)

function buscaMultiPadroes(padroes, texto, q) {
    const N = texto.length;
    const numPadroes = padroes.length;

    // Para cada padrão, é realizado uma busca
    for (let p = 0; p < numPadroes; p++) {
        const padrao = padroes[p];
        const M = padrao.length;
        let h = 1;
        let pHash = 0; // Hash do padrão
        let tHash = 0; // Hash da janela deslizante no texto

        // Valor de h para o hash do padrão e do texto
        for (let i = 0; i < M - 1; i++) {
            h = (h * d) % q;
        }

        // Calcula o hash do padrão e da primeira janela no texto
        for (let i = 0; i < M; i++) {
            pHash = (d * pHash + padrao.charCodeAt(i)) % q;
            tHash = (d * tHash + texto.charCodeAt(i)) % q;
        }

        // Desliza a janela sobre o texto
        for (let i = 0; i <= N - M; i++) {
            // Verifica se o hash do padrão e da janela deslizante são iguais
            if (pHash === tHash) {
                let j;
                // Verifica caractere por caractere para evitar colisões de hash
                for (j = 0; j < M; j++) {
                    if (texto[i + j] !== padrao[j]) {
                        break;
                    }
                }

                if (j === M) {
                    console.log(`Padrão "${padrao}" encontrado na posição ${i}`);
                }
            }

            // Calcula o hash para a próxima janela no texto
            if (i < N - M) {
                tHash = (d * (tHash - texto.charCodeAt(i) * h) + texto.charCodeAt(i + M)) % q;

                // Garante que o hash seja não-negativo
                if (tHash < 0) {
                    tHash = tHash + q;
                }
            }
        }
    }
}

const texto = "AABCAAADAABCAADAABCAA";
const padroes = ["AABC", "ADA", "CAADA", "AA", "AABCAAADA"];
const q = 101; // Um número primo para reduzir as colisões de hash

buscaMultiPadroes(padroes, texto, q);
