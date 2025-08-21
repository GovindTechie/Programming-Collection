#include <iostream>
#include <vector>

using namespace std;

class Stack {
private:
    vector<int> data;

public:
    bool isEmpty() {
        return data.empty();
    }

    void push(int value) {
        data.push_back(value);
        cout << value << " pushed\n";
    }

    void pop() {
        if (isEmpty()) {
            cout << "Stack Underflow\n";
            return;
        }
        cout << data.back() << " popped\n";
        data.pop_back();
    }

    void peek() {
        if (isEmpty()) {
            cout << "Stack is empty\n";
            return;
        }
        cout << "Top element is " << data.back() << "\n";
    }

    void display() {
        if (isEmpty()) {
            cout << "Stack is empty\n";
            return;
        }
        cout << "Stack elements: ";
        for (int i = data.size() - 1; i >= 0; i--) {
            cout << data[i] << " ";
        }
        cout << "\n";
    }
};

int main() {

    
    Stack s;

    s.push(10);
    s.push(20);
    s.push(30);
    s.peek();
    s.display();
    s.pop();
    s.display();

    return 0;
}
