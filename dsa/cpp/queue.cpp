# include<iostream>
# include<vector>
using namespace std;

class queue {
private:
    vector<int>data;
    int FrontIndex;
public:

    queue (){
        FrontIndex = 0;
    }
    void enqueue(int val) {
        data.push_back(val);
        cout << "Value " << val <<" Pushed to queue"<< endl;
    }

    bool isEmpty() {
        return FrontIndex >= data.size();
    }

    void dequeue() {
        if(isEmpty()) {
            cout<<"queue is empty" << endl;
            return;
        }
        cout << "Value " << data[FrontIndex] <<" from queue" << endl;
        FrontIndex++;
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is Empty\n";
            return;
        }

        cout << "Queue: ";
        for (int i = FrontIndex; i < data.size(); ++i)
            cout << data[i] << " ";
        cout << endl;
    }
};

int main() {
    queue q;

    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();

    q.dequeue();
    q.display();

    return 0;
}