const grafo = {
    1: [2, 4, 5],
    2: [1, 3, 5, 7, 9],
    3: [2, 6, 10, 12],
    4: [1, 5, 7],
    5: [1, 2, 5, 6, 8],
    6: [3, 5, 9, 11],
    7: [2, 4, 8],
    8: [5, 7, 9],
    9: [2, 6, 8, 10, 12],
    10: [3, 9, 11],
    11: [6, 10, 12],
    12: [3, 9, 11]
};

// DFS
function buscaProfundidade(grafo, inicio) {
    const visitados = new Set(); // O set serve para garantir que não haja vértices duplicados
    const resultado = [];
    const pilha = [inicio];

    while (pilha.length > 0) {
        const vertice = pilha.pop();  // Remove o vértice do topo da pilha
        if (!visitados.has(vertice)) {
            visitados.add(vertice);
            resultado.push(vertice);

            // Adiciona os vizinhos à pilha
            grafo[vertice].forEach(vizinho => {
                if (!visitados.has(vizinho)) {
                    pilha.push(vizinho);
                }
            });
        }
    }

    return resultado;
}


// BFS
function buscaLargura(grafo, inicio) {
    const visitados = new Set();  // O set serve para garantir que não haja vértices duplicados
    const fila = [inicio];
    const resultado = [];

    visitados.add(inicio); // Marca o vértice inicial como visitado

    while (fila.length > 0) {
        const vertice = fila.shift(); // Remove o primeiro vértice da fila
        resultado.push(vertice); // Adiciona o vértice ao resultado

        // Percorre todos os vizinhos do vértice atual
        grafo[vertice].forEach(vizinho => {
            if (!visitados.has(vizinho)) {
                visitados.add(vizinho);
                fila.push(vizinho);
            }
        });
    }

    return resultado;
}

const resultadoDFS = buscaProfundidade(grafo, 1);
const resultadoBFS = buscaLargura(grafo, 1);

console.log("Resultado DFS:", resultadoDFS);
console.log("Resultado BFS:", resultadoBFS);
