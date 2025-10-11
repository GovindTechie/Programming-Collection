#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double weight{7.4};
    
    //floor used to remove decimal point 7.4 -> 7
    cout << "Weight rounded to floor is : " << floor(weight) << endl; 

    //ceil used to remove decimal point and take next value 7.4 -> 8
    cout << "Weight rounded to ceil is : " << ceil(weight) << endl;

    double saving {-5000};

    //abs
    cout << "abs of weight is : " << abs(weight) << endl;
    cout << "abs of saving is : " << abs(saving) << endl;

    //exponential 
    double exponential = exp(10);
    cout << "The exponential of 10 is : " << exponential << endl;

    //power of number
    cout << "3^4 is : " << pow(3, 4) << endl;

    //log fuction
    cout << "e to power of what so we get 54.59 : " << log(54.59) << endl;
    cout << "10 to the power of what so we get 10000 : " << log10(10000) << endl;

    //square root 
    cout << "square root of 81 is : " << sqrt(81) << endl;

    //round
    cout << "3.754 rounded to : " << round(3.754) << endl;
    cout << "4.5 rounded to : " << round(4.5) << endl;
    cout << "4.4 rounded to : " << round(4.4) << endl;





    return 0;
}