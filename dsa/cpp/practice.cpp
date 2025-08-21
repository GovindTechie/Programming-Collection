# include<iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
};

Node* createNode(int value) {
    Node* newNode = new Node;
    newNode->data = value;
    newNode->next = nullptr;
    return newNode;
}

void printlist(Node* head) {
    Node* temp = head;
    while(temp != nullptr) {
        cout << temp->data << " -> ";
        temp = temp -> next;
    }
    cout << "NULL" << endl;
}


int main () {
    Node* head = createNode(10);
    head->next = createNode(20);
    head->next->next = createNode(30);
   
    printlist(head);
    
    return 0;

}