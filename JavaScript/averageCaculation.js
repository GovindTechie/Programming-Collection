let arr_marks = [95, 83, 89, 99, 95];
let sum = 0;

for (let value of arr_marks){
    sum += value;
}

let avg = (sum/arr_marks.length)
console.log(avg)