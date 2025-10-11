#include <iostream>
using namespace std;

int main() {
    
    int num;
    cout << "Enter a number ";
    cin >> num;
    if(num < 2){
        cout << "the number " << num << " is not prime number" << endl;
    }
    else {
        bool isPrime = true;
        for(size_t i{2}; i*i <= num; i++) {
            if(num % i == 0) {
                cout << "the number " << num << " is not prime number " << endl;
                isPrime = false;
                break;
            }

        }
        if (isPrime) {
            cout << "the number " << num << " is prime number " << endl;
        }
    }
    cout << "done , program ended" << endl;

    return 0;
}
