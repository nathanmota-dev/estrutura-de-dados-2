function RecursiveMultiple(a, b) {
    if (b === 0) {
        return 0;
    } else {
        return a + RecursiveMultiple(a, b - 1);
    }
}

a = 5
b = 10

result = RecursiveMultiple(a, b)
console.log(result);