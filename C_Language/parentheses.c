#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct stack {
  char data;
  struct stack *next;
};

//Traversing linked List
void linkedListTraversal(struct stack *top) {
  struct stack *ptr = top;
  while(ptr != NULL) {
    printf("Elements are : %c\n",ptr -> data);
    ptr = ptr -> next;
  }
}

//where stack is empty 
int isEmpty(struct stack *top) {
  if(top == NULL) {
    return 1;
  }
 return 0;
}

//Pushing element into the stack
struct stack *push(struct stack *top, char data) {
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
    printf("\nParentheses is not matching");
    exit(1);
  }
  else {
    struct stack *ptr = top;
    top = ptr -> next;
    free(ptr);
    return top;
    }
}

int main()
{
  int n;
  struct stack *top = NULL;
  printf("Enter size of string\n");
  scanf("%d",&n);
  while (getchar() != '\n'); 
  char s[n];
  printf("Enter Expression\n");
  fgets(s,n,stdin);
  printf("You entered: %s\n", s);
  for(int i=0; (s[i])!='\0'; i++ ) {
    if(s[i] == '(') {
      printf("(\t");
      top = push(top,'(');
    }
    if(s[i] == ')') {
      printf(")\t");
      top = pop(top);
    }
  }
  printf("\nParentheses is matching");
  return 0;
}