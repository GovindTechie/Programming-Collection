#include <stdio.h>
#include <stdlib.h>

struct node {
  int data;
  struct node *next;
};

void linkedListTraversal(struct node *ptr) {
  while (ptr != NULL){
    printf("Element : %d\n",ptr->data);
    ptr = ptr->next;
  }
}
int main()
{
  struct node *head;
  struct node *second;
  struct node *third;
  struct node *fourth;
  struct node *fifth;
  struct node *sixth;
  struct node *seventh;
  struct node *eighth;
  struct node *ninth;
  struct node *tenth;
  
  head = (struct node *)malloc (sizeof(struct node));
  second = (struct node *)malloc (sizeof(struct node));
  third = (struct node *)malloc (sizeof(struct node));
  fourth = (struct node *)malloc (sizeof(struct node));
  sixth = (struct node *)malloc (sizeof(struct node));
  fifth = (struct node *)malloc (sizeof(struct node));
  seventh = (struct node *)malloc (sizeof(struct node));
  eighth = (struct node *)malloc (sizeof(struct node));
  ninth = (struct node *)malloc (sizeof(struct node));
  tenth = (struct node *)malloc (sizeof(struct node));
  
  head -> data = 7;
  head -> next = second;
  
  second-> data = 71;
  second  -> next = third;
  
  third -> data = 17;
  third -> next = fourth;
  
  fourth -> data = 27;
  fourth -> next = fifth;
  
  fifth -> data = 14;
  fifth -> next = sixth;
  
  sixth -> data = 44;
  sixth -> next = seventh;
  
  seventh -> data = 62;
  seventh -> next = eighth;
  
  eighth -> data = 81;
  eighth -> next = ninth;
  
  ninth -> data = 99;
  ninth -> next = NULL;
  
  linkedListTraversal(head);
  
  return 0;
}