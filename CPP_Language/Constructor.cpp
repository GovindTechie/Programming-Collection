#include <iostream>
using namespace std;

class Car {
public:
    int speed;

    // Default constructor
    Car() {
        speed = 0;
        cout << "Car created with default speed " << speed << endl;
    }

    // Parameterized constructor
    Car(int s) {
        speed = s;
        cout << "Car created with speed " << speed << endl;
    }

    // Destructor
    ~Car() {
        cout << "Car destroyed" << endl;
    }
};

int main() {
    Car c1;       // default constructor
    Car c2(100);  // parameterized constructor

    return 0; // destructor called automatically
}
