# include<iostream>
# include<iomanip>
using namespace std;

int main() {
    int width = 20;
    cout << left;
    cout<<setw(width)<<"last_name" << setw(width) << "first_name" << endl;
    cout << internal;
    cout<<setw(width)<<"khedkar" << setw(width) <<"govind" << endl;
    cout << showpos;
    cout << true << endl;
    cout << boolalpha;
    cout <<true << endl;
    return 0;
}