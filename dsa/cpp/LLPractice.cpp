#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;

    Node(int value){
         data = value;
        next = nullptr;
    }
};

class LinkedList
{
private:
    Node *head;

public:
    LinkedList()
    {
        head = nullptr;
    }

    void createNode(int value)
    {
        Node *newNode = new Node(value);

        if (head == nullptr)
        {
            head = newNode;
        }
        else
        {
            Node *temp = head;
            while (temp->next != nullptr)
                temp = temp->next;
            temp->next = newNode;
        }
    }

    void printList()
    {
        Node *temp = head;
        while (temp != nullptr)
        {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "Null";
    }
};

int main()
{
    LinkedList list;
    list.createNode(10);
    list.createNode(20);
    list.createNode(30);

    list.printList();

    return 0;
}