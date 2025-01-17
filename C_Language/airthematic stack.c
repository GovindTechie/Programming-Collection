#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define STACKSIZE 100

struct stack {
    int top;
    int items[STACKSIZE];
};

int empty(struct stack *ps);
int pop(struct stack *ps);
void push(struct stack *ps, int x);
int operation(char c, int opd1, int opd2);

int empty(struct stack *ps) {
    return (ps->top == -1);
}

int pop(struct stack *ps) {
    if (empty(ps)) {
        printf("Stack underflow\n");
        exit(0);
    } else {
        return ps->items[ps->top--];
    }
}

void push(struct stack *ps, int x) {
    if (ps->top == STACKSIZE - 1) {
        printf("Stack overflow\n");
        exit(0);
    } else {
        ps->items[++ps->top] = x;
    }
}

int operation(char op, int opd1, int opd2) {
    int result;
    switch (op) {
        case '+':
            result = opd1 + opd2;
            break;
        case '-':
            result = opd1 - opd2;
            break;
        case '*':
            result = opd1 * opd2;
            break;
        case '/':
            if (opd2 == 0) {
                printf("Error: Division by zero\n");
                exit(0);
            }
            result = opd1 / opd2;
            break;
        case '^':
            result = (int)pow(opd1, opd2);
            break;
        default:
            printf("Error: Invalid operator\n");
            exit(0);
    }
    return result;
}

int main() {
    struct stack s;
    s.top = -1;

    FILE *file = fopen("infile.txt", "r");
    if (file == NULL) {
        printf("Error: Unable to open input file\n");
        return 1;
    }
    
    char c;
    int res;

    c = fgetc(file);

    while (!feof(file)) {
        if (c == ' ' || c == '\r' || c == '\n') {
            // Do nothing, skip whitespace
        } else if (c >= '0' && c <= '9') {
            // Convert the character to an integer and push it onto the stack
            int num = c - '0';
            push(&s, num);
        } else if (c == '+' || c == '-' || c == '*' || c == '/' || c == '^') {
            // Pop the top two numbers from the stack, perform the operation, and push the result back
            int opd2 = pop(&s);
            int opd1 = pop(&s);
            int result = operation(c, opd1, opd2);
            push(&s, result);
        } else {
            printf("Invalid character in the expression: %c\n", c);
            exit(0);
        }
        c = fgetc(file);
    }

    res = pop(&s);
    printf("Final result is %d\n", res);

    fclose(file);
    return 0;
}