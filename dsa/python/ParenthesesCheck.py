class Stack :
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)
        print(f"Pushed {val}")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty can't pop")
            return None
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    
    def display(self):
        print(f"The stack from top to bottom is : {self.stack[::-1]}")

    def peek(self):
        if self.isEmpty():
            print("Stack is empty can't peek")
            return None
        print(self.stack[-1])

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(40)
stack.push(30)
print(f"Poped {stack.pop()}")
stack.push(20)
print(f"Peeked {stack.peek()}")
stack.display()

    