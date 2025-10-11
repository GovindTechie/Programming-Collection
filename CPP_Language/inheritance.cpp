#include <iostream>
using namespace std;

class Person {
public:
    string name;
    int age;
};

class Student : public Person {
public:
    int rollNo;
    
    void getInto(){
        cout << "Name : " << name << endl;
        cout << "Age : " << age << endl;
        cout << "Roll no : " << rollNo << endl;

    }
};

int main() {
    Student s1;
    s1.age = 21;
    s1.name = "Govind";
    s1.rollNo = 73;
    s1.getInto();
    return 0;
}
