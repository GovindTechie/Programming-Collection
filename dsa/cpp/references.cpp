#include <iostream>
using namespace std;

int main() {
    
    int int_data{33};
    double double_data{55};

    // reference
    int& ref_int_data{int_data};
    double& ref_double_data{double_data};



    cout << "value of int_data : " << int_data << endl;
    cout << "value of double_data : " << double_data << endl;
    cout << "value of ref_int_data : " << ref_int_data << endl;
    cout << "value of ref_double_data : " << ref_double_data << endl;
    cout << "address of int_data : " << &int_data << endl;
    cout << "address of ref_int_data : " << &ref_int_data << endl;


    
    return 0;
}