#include <stdio.h>
#include <stdlib.h>

struct stack {
  int data;
  struct stack *next;
};

//Traversing linked List
void linkedListTraversal(struct stack *top) {
  struct stack *ptr = top;
  while(ptr != NULL) {
    printf("Elements are : %d\n",ptr -> data);
    ptr = ptr -> next;
  }
}

//where stack is empty 
int isEmpty(struct node *top) {
  if(top == NULL) {
    return 1;
  }
 return 0;
}

//Pushing element into the stack
struct stack *push(struct stack *top, int data) {
  struct stack *ptr = (struct stack *)malloc(sizeof(struct stack)); 
  if(ptr == NULL) {
    printf("Stack Overflow");
    return top;
  }
      ptr -> data = data;
      ptr -> next = top;
      top = ptr;
      return top;
}

//Poping element from the stack
struct stack *pop(struct stack *top) {
  if(isEmpty(top)) {
    printf("Stack Underflow");
  }
  else {
    struct stack *ptr = top;
    top = ptr -> next;
    printf("The element %d is popped\n",ptr -> data);
    free(ptr);
    return top;
    }
}

int main()
{
  struct stack *top = NULL;
  top = push(top,2);
  top = push(top,4);
  top = push(top,6);
  top = push(top,8);
  top = pop(top);
  linkedListTraversal(top);
  return 0;
}