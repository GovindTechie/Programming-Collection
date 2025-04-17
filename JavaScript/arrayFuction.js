let myArr = [10, 20, 30, 40];

// Push - Add element to the end
myArr.push(50);
console.log("After push(50):", myArr);

// Pop - Remove element from the end
let removedLast = myArr.pop();
console.log("After pop():", myArr);
console.log("Popped value:", removedLast);

// Unshift - Add element to the beginning
myArr.unshift(5);
console.log("After unshift(5):", myArr);

// Shift - Remove element from the beginning
let removedFirst = myArr.shift();
console.log("After shift():", myArr);
console.log("Shifted value:", removedFirst);



let arr = [100, 200, 300, 400, 500];

// 🔹 slice(start, end) - does NOT change original array
let slicedArr = arr.slice(1, 4);  // takes elements at index 1 to 3
console.log("Original array after slice():", arr);
console.log("Sliced array (1 to 3):", slicedArr);

// 🔹 splice(start, deleteCount, item1, item2, ...) - modifies original array

// Remove 2 elements from index 2 and insert 999 & 888
let splicedItems = arr.splice(2, 2, 999, 888);
console.log("Original array after splice():", arr);
console.log("Removed elements with splice():", splicedItems);
