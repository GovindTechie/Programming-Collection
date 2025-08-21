#include <stdio.h>
#include <stdlib.h>



struct Node
{
    int data;
    struct Node *next;
};




void linkeListTraversal(struct Node *head)
{
    struct Node *curr = head;
    while (curr != NULL)
    {
        printf("%d ", curr->data);
        curr = curr->next;
    }
}

struct Node* create(int data) {
    struct Node* temp = (struct Node*) malloc(sizeof(struct Node));
    temp->data = data;
    temp->next = NULL;
    return temp;
}




int main()
{
    
    struct Node* node1 = create(10);
    struct Node* node2 = create(20);
    struct Node * node3 = create(30);

    node1->next = node2;
    node2->next = node3;

    linkeListTraversal(node1);
    return 0;
}