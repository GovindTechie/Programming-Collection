#include <iostream>
using namespace std;

class Animal {
public:
    virtual void sound() = 0; 
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "dog is barking bhuk bhok bhok";
    }
};

int main() {
    
    Dog *d = new Dog(); 
    d->sound();
}
