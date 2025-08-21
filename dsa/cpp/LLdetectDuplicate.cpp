#include <iostream>
#include <unordered_set>
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

bool detectDuplicate(Node *head)
{
    Node *temp = head;
    unordered_set<int> seen;
    while (temp != nullptr)
    {
        if (seen.count(temp->data))
        {
            return true;
        }
        seen.insert(temp->data);
        temp = temp->next;
    }
    return false;
}

int main()
{
    Node *head = createNode(20);
    head->next = createNode(30);
    head->next->next = createNode(40);
    head->next->next->next = createNode(30);
    head->next->next->next->next = createNode(20);

    printList(head);
    cout << boolalpha << "Is duplicate in list : " << detectDuplicate(head) << endl;

    return 0;
}