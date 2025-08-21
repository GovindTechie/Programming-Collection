#include <stdio.h>
#define MAX 100

typedef struct {
    int data[MAX];
    int top;
} Stack;

void initialize(Stack *s) {
    s->top = -1;
}

int isEmpty(Stack *s) {
    return s->top == -1;
}

int isFull(Stack *s) {
    return s->top == MAX - 1;
}

void push(Stack *s, int value) {
    if (isFull(s)) {
        printf("Push Failed: Stack Overflow\n");
        return;
    }
    s->data[++(s->top)] = value;
    printf("Pushed: %d\n", value);
}

void pop(Stack *s) {
    if (isEmpty(s)) {
        printf("Pop Failed: Stack Underflow\n");
        return;
    }
    int popped = s->data[(s->top)--];
    printf("Popped: %d\n", popped);
}

void peek(Stack *s) {
    if (isEmpty(s)) {
        printf("Peek Failed: Stack is Empty\n");
        return;
    }
    printf("Top Element: %d\n", s->data[s->top]);
}

void size(Stack *s) {
    printf("Current Size: %d\n", s->top + 1);
}

void display(Stack *s) {
    if (isEmpty(s)) {
        printf("Display: Stack is Empty\n");
        return;
    }
    printf("Stack Elements (Top to Bottom): ");
    for (int i = s->top; i >= 0; i--) {
        printf("%d ", s->data[i]);
    }
    printf("\n");
}

int main() {
    Stack s;
    initialize(&s);

    push(&s, 10);
    push(&s, 20);
    push(&s, 30);

    display(&s);
    size(&s);
    peek(&s);

    pop(&s);
    peek(&s);
    size(&s);
    display(&s);

    return 0;
}
