#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node(int val)
    {
        data = val;
        next = nullptr;
    }
};

Node *createNode(int value)
{
    Node *newNode = new Node(value);
    return newNode;
}

bool isPalindrome(Node *head)
{
    Node *fast = head;
    Node *slow = head;
    Node *mid;
    while (fast && fast->next)
    {
        fast = fast->next->next;
        slow = slow->next;
    }
    if (fast)
    {
        mid = slow->next;
    }
    else
    {
        mid = slow;
    }
    // making second half reverse
    Node *curr = mid;
    Node *prev = nullptr;
    Node *curnext = nullptr;
    while (curr != nullptr)
    {
        curnext = curr->next;
        curr->next = prev;
        prev = curr;
        curr = curnext;
    }
    Node *temp = head;
    while (prev != nullptr)
    {
        if (temp->data != prev->data)
        {
            return false;
        }
        temp = temp->next;
        prev = prev->next;
    }
    return true;
}

void printList(Node *head)
{
    Node *temp = head;
    while (temp != nullptr)
    {
        cout << temp->data << " -> ";
        temp = temp->next;
    }
    cout << "NULL" << endl;
}

int main()
{
    Node *head = createNode(1);
    head->next = createNode(2);
    head->next->next = createNode(2);
    head->next->next->next = createNode(1);
    // head->next->next->next->next = createNode(2);

    printList(head);

    cout << boolalpha << "Is list is palindrome : " << isPalindrome(head) << endl;

    return 0;
}