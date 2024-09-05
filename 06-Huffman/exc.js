class No {
    constructor(caractere, frequencia) {
        this.caractere = caractere;
        this.frequencia = frequencia;
        this.esquerda = null;
        this.direita = null;
    }
}

function calculaFrequencias(texto) {
    // Calcula a frequência de cada caractere no texto
    const frequencias = {};
    for (let caractere of texto) {
        frequencias[caractere] = (frequencias[caractere] || 0) + 1;
    }
    return frequencias;
}

function constroiArvore(frequencias) {
    // Constrói a árvore de Huffman
    let fila = Object.entries(frequencias).map(([caractere, frequencia]) => new No(caractere, frequencia));

    while (fila.length > 1) {
        fila.sort((a, b) => a.frequencia - b.frequencia);
        const esquerda = fila.shift();
        const direita = fila.shift();

        const pai = new No(null, esquerda.frequencia + direita.frequencia);
        pai.esquerda = esquerda;
        pai.direita = direita;

        fila.push(pai);
    }

    return fila[0];
}

function codificaArvore(arvore, codigo = '', codigos = {}) {
    // Gera o código binário para cada caractere
    if (arvore.caractere) {
        codigos[arvore.caractere] = codigo;
    } else {
        codificaArvore(arvore.esquerda, codigo + '0', codigos);
        codificaArvore(arvore.direita, codigo + '1', codigos);
    }
    return codigos;
}

function codificaTexto(texto, codigos) {
    // Codifica o texto usando os códigos gerados
    return texto.split('').map(caractere => codigos[caractere]).join('');
}

function decodificaTexto(textoCodificado, arvore) {
    // Decodifica o texto codificado percorrendo a árvore de Huffman
    let textoDecodificado = '';
    let noAtual = arvore;

    for (let bit of textoCodificado) {
        noAtual = bit === '0' ? noAtual.esquerda : noAtual.direita;

        if (noAtual.caractere) {
            textoDecodificado += noAtual.caractere;
            noAtual = arvore;
        }
    }

    return textoDecodificado;
}

function comprime(texto) {
    // Função principal para compressão
    const frequencias = calculaFrequencias(texto);
    const arvore = constroiArvore(frequencias);
    const codigos = codificaArvore(arvore);
    const textoCodificado = codificaTexto(texto, codigos);
    return { textoCodificado, arvore };
}

function descomprime(textoCodificado, arvore) {
    // Função principal para descompressão
    return decodificaTexto(textoCodificado, arvore);
}

// Exemplo de uso
const texto = "O rato roeu a roupa do rei de roma";
const { textoCodificado, arvore } = comprime(texto);

console.log("Texto codificado:", textoCodificado);
const textoDecodificado = descomprime(textoCodificado, arvore);
console.log("Texto decodificado:", textoDecodificado);
