vowels = (str) => {
    let count = 0;
    for (let char of str) {
        if (char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u' ||
        char == 'A' || char == 'E' || char == 'I' || char == 'O' || char == 'U') {
            count += 1;
        }
    }
    return count
}


console.log(`The number of vowels is : ${vowels("i am govind khedkar")}`);  