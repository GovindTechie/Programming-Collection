# include <iostream>
# include <vector>
using namespace std;

class MinStack {
private:
    vector<int>stack;
    vector<int>MinStack;
public:  
    void push(int val) {
       stack.push_back(val);
       if(MinStack.empty() || MinStack.back() >= stack.back()){
        MinStack.push_back(val);
       }else {
        MinStack.push_back(MinStack.back());
       }
    }
    
    void pop() {
        stack.pop_back();
        MinStack.pop_back();
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return MinStack.back();
    }
};


//  Your MinStack object will be instantiated and called as such:
int main () {
    MinStack* obj = new MinStack();
    // obj->push(val);
    obj->pop();
    int param_3 = obj->top();
    int param_4 = obj->getMin();
    return 0;
}

 