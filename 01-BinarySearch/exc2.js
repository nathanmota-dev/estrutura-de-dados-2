class BinarySearchTree {
    constructor(nodeValue, left = null, right = null) {
        this.nodeValue = nodeValue;
        this.left = left;
        this.right = right;
    }

    insert(nodeValue) {
        if (nodeValue >= this.nodeValue) {
            // Insere valor na direita
            if (this.right) {
                this.right.insert(nodeValue);
            } else {
                this.right = new BinarySearchTree(nodeValue);
            }
        } else {
            // Insere valor na esquerda
            if (this.left) {
                this.left.insert(nodeValue);
            } else {
                this.left = new BinarySearchTree(nodeValue);
            }
        }
    }

    findAllOccurrences(value, positions = [], checks = 0, currentPosition = 0) {
        checks++; // Incrementa o contador de verificações

        if (value === this.nodeValue) {
            positions.push(currentPosition); // Armazena a posição onde o valor foi encontrado
        }

        if (this.left) {
            // Busca à esquerda
            const resultLeft = this.left.findAllOccurrences(value, positions, checks, currentPosition + 1);
            checks = resultLeft.checks;
            positions = resultLeft.positions;
        }

        if (this.right) {
            // Busca à direita
            const resultRight = this.right.findAllOccurrences(value, positions, checks, currentPosition + 1);
            checks = resultRight.checks;
            positions = resultRight.positions;
        }

        return { positions, checks }; // Retorna as posições e o número de verificações
    }    
}


const randomNumbers = Array(100).fill(0).map(() => Math.floor(Math.random() * 101));
console.log(randomNumbers);

const tree = new BinarySearchTree(randomNumbers[0]);
for (let i = 1; i < randomNumbers.length; i++) {
    tree.insert(randomNumbers[i]);
}

// Solicita ao usuário o valor a ser buscado
const readlineSync = require('readline-sync');

const valueToFind = parseInt(readlineSync.question("Digite o valor que deseja buscar:"), 10);

// Encontra todas as ocorrências do valor na árvore
const result = tree.findAllOccurrences(valueToFind);

if (result.positions.length > 0) {
    console.log(`Valor ${valueToFind} encontrado ${result.positions.length} vezes nas posições: ${result.positions.join(', ')}.`);
    console.log(`Número total de verificações: ${result.checks}`);
} else {
    console.log(`Valor ${valueToFind} não encontrado na árvore após ${result.checks} verificações.`);
}
