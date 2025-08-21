#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
};

Node *createNode(int val)
{
    Node *newNode = new Node;
    newNode->data = val;
    newNode->next = nullptr;
    return newNode;
}

void printList(Node *head)
{
    Node *temp = head;
    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NUll" << endl;
}

int middeleReturn(Node *head)
{
    Node* fast = head;
    Node* slow = head;
    while(fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    int mid = slow->data;
    return mid;
//     Node *temp = head;
//     int count = 0;
//     while (temp != nullptr)
//     {
//        count++;
//        temp = temp->next;
//     }

//     int mid = count/2;

//     Node *temp1 = head;
//     for (int i=0; i<mid; i++) {
//         temp1 = temp1->next;
//     }
//     return temp1->data;
}

int main()
{
    Node *head = createNode(20);
    head->next = createNode(30);
    head->next->next = createNode(40);
    head->next->next->next = createNode(30);
    head->next->next->next->next = createNode(20);
    // head->next->next->next->next->next = createNode(90);

    printList(head);
    cout  << "Middle Turm of list is  : " << middeleReturn(head) << endl;

    return 0;
}