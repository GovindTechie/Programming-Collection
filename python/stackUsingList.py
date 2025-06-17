class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "stack is empty"
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
s = Stack()
s.push(20)
s.push(30)
s.push(56)

print(f"Stack after pushes:  {s.stack}")
print(f"Poped Element : {s.pop()}")
print(f"Top Element : {s.peek()}")
print(f"Is stack empty ? : {s.is_empty()}")
print(f"Stack size: {s.size()}")
