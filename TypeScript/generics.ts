function wrap<T>(value: T): T {
  return value;
}

console.log(wrap(10));        // number
console.log(wrap("Govind"));  // string
