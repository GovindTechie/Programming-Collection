// we are creating a program that convert decimal number into binary number

#include<iostream>
using namespace std;


int decToBinary (int decNum) {
    int ans = 0, pow = 1, rem;

    while(decNum > 0){
        rem = decNum % 2;
        decNum = decNum/2;

        ans += (rem * pow);
        pow = pow * 10;
    }

return ans;

}

int main (){
    int decNum;
    cout << "Enter number that you want to convert to binary" << endl;
    cin >> decNum;
    cout<< decToBinary(decNum) << endl;
    return 0;
}