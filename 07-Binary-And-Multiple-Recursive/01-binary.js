function recursiveBinary(n) {
    if (n > 1) {
        recursiveBinary(Math.floor(n / 2)); 
    }
    process.stdout.write(String(n % 2)); // Imprime na mesma linha
}

let numero = 10;
recursiveBinary(numero);
console.log(); 
