#include <iostream>
#include <string>
using namespace std;



const int Pen {10};
const int Marker {20};
const int Earser {30};
const int Rectangle {40};
const int Circle {50};
const int Ellipse {60};

int main() {

    int tool {10};
    switch(tool) {
        case Pen : {
            cout << "Pen is tool as selected";
            break;
        }
        case Marker : {
            cout << "Marker is tool as selected";
            break;
        }
        case Earser : {
            cout << "Earser is tool as selected";
            break;
        }
        case Rectangle : {
            cout << "Rectangle is tool as selected";
            break;
        }
        case Circle : {
            cout << "Circle is tool as selected";
            break;
        }
        case Ellipse : {
            cout << "Ellipse is tool as selected";
            break;
        }
        default : {
            cout << "tools not matching with anything so change tool";
        }


    }
    return 0;
}