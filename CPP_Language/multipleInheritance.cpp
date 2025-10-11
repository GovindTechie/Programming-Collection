#include <iostream>
using namespace std;

class A {
public:
    void greet() { cout << "Hello from A\n"; }
};

class B {
public:
    void greet() { cout << "Hello from B\n"; }
};

class C : public A, public B {
public:
    void greet() { cout << "Hello from c\n"; }
};

int main() {
    C obj;
    obj.greet(); 
}
