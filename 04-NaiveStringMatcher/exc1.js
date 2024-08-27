function stringSearch(string, pattern, joker) {
    let count = 0;

    for (let i = 0; i <= string.length - pattern.length; i++) {
        let match = true;
        for (let j = 0; j < pattern.length; j++) {
            if (pattern[j] !== joker && pattern[j] !== string[i + j]) {
                match = false;
                break;
            }
        }
        if (match) count++;
    }

    return count;
}

console.log(stringSearch("akgjfjhuyutomatokajkmhgsvkjrtomato", "*oma*o", "*"));
