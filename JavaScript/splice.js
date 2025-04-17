let companies = ['Bloomberg', 'Microsoft', 'Uber', 'Google', 'IBM', 'Netflix'];

console.log(`The companies are : ${companies}`);
deleteFirst = companies.shift();

console.log(`After deleting first name companies are : ${companies}\nDeleted company : ${deleteFirst}`);

let indexOFUber = companies.indexOf('Uber');

companies.splice(indexOFUber, 1, 'Ola');

console.log(`After replacing Uber with Ola companies are : ${companies}`);
