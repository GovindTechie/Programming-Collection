let pricesOfItem = [250, 645, 300, 900, 50];
let result = [];
let discount = 0, item = 0;
for (let val of pricesOfItem) {
    discount = val/10;
    item = val - discount;
    result.push(item);
}

console.log(`Original prices of items : ${pricesOfItem}`)
console.log(`after 10% discount prices : ${result}`)