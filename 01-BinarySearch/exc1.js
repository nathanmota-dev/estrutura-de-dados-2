// Gerando números aleatórios entre 0 e 100
const randomNumbers = Array(100).fill(0).map(() => Math.floor(Math.random() * 101));
console.log(randomNumbers);

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

    getMinValue() {
        // encontrar o menor valor na subárvore
        if (this.left) {
            return this.left.getMinValue();
        } else {
            return this.nodeValue;
        }
    }

    remove(value, parent = null) {
        if (value > this.nodeValue) {
            // O nó que precisamos remover está à direita
            if (this.right) {
                this.right.remove(value, this);
            }
        } else if (value < this.nodeValue) {
            // O nó que precisamos remover está à esquerda
            if (this.left) {
                this.left.remove(value, this);
            }
        } else {
            // Encontramos o nó que precisamos remover
            if (this.left && this.right) { // Tem dois filhos
                this.nodeValue = this.right.getMinValue();
                this.right.remove(this.nodeValue, this);
            } else if (!parent) { // É o nó raiz da árvore
                if (this.left) { // Tem filho à esquerda
                    this.nodeValue = this.left.nodeValue;
                    this.right = this.left.right;
                    this.left = this.left.left;
                } else if (this.right) { // Tem filho à direita
                    this.nodeValue = this.right.nodeValue;
                    this.left = this.right.left;
                    this.right = this.right.right;
                }
            } else if (parent.left === this) { // O ponteiro que o nó está ligado é o da esquerda
                parent.left = this.left ? this.left : this.right; // Liga o filho ao ponteiro do pai
            } else if (parent.right === this) { // O ponteiro que o nó está ligado é o da direita
                parent.right = this.right ? this.right : this.left; // Liga o filho ao ponteiro do pai
            }
        }
    }    

    contains(value, checks = 0) {
        checks++; // Incrementa o contador de verificações
        if (value === this.nodeValue) {
            return { found: true, checks }; // Retorna que o valor foi encontrado e o número de verificações
        }

        if (value > this.nodeValue) {
            if (this.right) {
                return this.right.contains(value, checks); // Busca à direita
            } else {
                return { found: false, checks }; // Não encontrado à direita
            }
        } else {
            if (this.left) {
                return this.left.contains(value, checks); // Busca à esquerda
            } else {
                return { found: false, checks }; // Não encontrado à esquerda
            }
        }
    }    
}

// Cria a árvore e insere os números aleatórios
const tree = new BinarySearchTree(randomNumbers[0]);
for (let i = 1; i < randomNumbers.length; i++) {
    tree.insert(randomNumbers[i]);
}

// Solicita ao usuário o valor a ser buscado
const readlineSync = require('readline-sync');

const valueToFind = parseInt(readlineSync.question("Digite o valor que deseja buscar:"), 10);

// Verifica se o valor está na árvore
const result = tree.contains(valueToFind);
if (result.found) {
    console.log(`Valor ${valueToFind} encontrado após ${result.checks} verificações.`);
} else {
    console.log(`Valor ${valueToFind} não encontrado na árvore após ${result.checks} verificações.`);
}
