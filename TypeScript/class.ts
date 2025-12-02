class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, I am ${this.name} and I am ${this.age}`);
  }
}

const p = new Person("Govind", 22);
p.greet();
