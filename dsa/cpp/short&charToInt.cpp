#include <iostream>
using namespace std;

int main() {

    short int var1{20};
    short int var2 {30};
    char var3 = 'g';
    char var4 = 'k';

    cout << "size of var1 is : " << sizeof(var1) << " & type is : " << typeid(var1).name() << endl;
    cout << "size of var3 is : " << sizeof(var3) << " & type is : " << typeid(var3).name() << endl;

    short int result  = var1 + var2;
    auto result2 = var1 + var2;
    auto result3 = var3 + var4;

    cout << "size of result is : " << sizeof(result) << " & type is : " << typeid(result).name()  << endl;
    cout << "size of result2 is : " << sizeof(result2) << " & type is : " << typeid(result2).name()  << endl;
    cout << "size of result3 is : " << sizeof(result3) << " & type is : " << typeid(result3).name()  << endl;
    cout << result3;



    return 0;
}