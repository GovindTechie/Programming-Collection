# include <iostream>
# include <vector>
using namespace std;

class MyQueue {
private:
    vector<int>stack1;
    vector<int>stack2; 
public: 
    void push(int x) {
        stack1.push_back(x);
    }
    
    int pop() {
        if(stack2.empty()) {
            if(stack1.empty()) {
                return -1;
            }
            while(!stack1.empty()) {
                stack2.push_back(stack1.back());
                stack1.pop_back();
            }
        }
        int popped = stack2.back();
        stack2.pop_back();
        return popped;
    }
    
    int peek() {
        if(stack2.empty()) {
            if(stack1.empty()) {
                return -1;
            }
            while(!stack1.empty()) {
                stack2.push_back(stack1.back());
                stack1.pop_back();
            } 
        }
        return stack2.back();
    }
    
    bool empty() {
        return stack1.empty() && stack2.empty();
    }
    
    void display() {
        if(stack2.empty()) {
            if(stack1.empty()) {
                cout << "Queue is empty" << endl;
            }
            while(!stack1.empty()) {
                stack2.push_back(stack1.back());
                stack1.pop_back();
            }
        }  
        cout << "Stack element are : ";
        for(int i=stack2.size() -1; i>=0; i--) {
            cout << stack2[i] << " ";
        }  

        for(int i=0; i<stack1.size(); i++) {
            cout << stack1[i] << " ";
        }  
        cout << endl; 
    }
};

int main() {
    MyQueue* obj = new MyQueue();
    obj-> push(10);
    obj-> push(20);
    obj-> push(54);
    obj-> push(65);
    obj-> push(75);
    cout << "the pop value is : " << obj -> pop() << endl;
    cout << "the peek value is :" << obj -> peek() << endl;
    cout << "is The queue is empty " << obj -> empty() << endl;

    obj -> display();

    return 0;
}
