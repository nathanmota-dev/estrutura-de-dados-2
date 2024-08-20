function bubbleSort(arr) {
    let n = arr.length;
    let cost = 0; // Variável para rastrear o custo de execução

    // O algoritmo Bubble Sort
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            // Comparação entre elementos adjacentes
            cost += 1;

            if (arr[j] > arr[j + 1]) {
                // Troca dos elementos
                let temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                // Custo da troca
                cost += 3; // Considerando 3 operações: 1 para armazenar em temp, 2 para a troca
            }
        }
    }

    return { sortedArray: arr, cost: cost };
}

// Aplicando
let arr = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]; // Pior caso (array em ordem decrescente)
let result = bubbleSort(arr);

console.log("Array ordenado:", result.sortedArray);
console.log("Custo de Execução (T(n)):", result.cost);
