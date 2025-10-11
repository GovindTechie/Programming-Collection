# include <bits/stdc++.h>
using namespace std;


class Myclass {
public:
    string name = "Govind Khedkar";
    int age = 22;

    void printing() {
        cout << name << " " << age << endl;
    }
};


int main() {
    Myclass classer;
    classer.printing();
}