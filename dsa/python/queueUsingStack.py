class queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)
        print(f"The {val} is enqueued")
        return
    
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                print("Can't dequeue stack is empty")
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        popValue = self.stack2.pop()
        print(f"The dequeueed value is {popValue}")

    def isEmpty(self):
        return not self.stack1 and not self.stack2
    
    def peek(self) :
        if not self.stack2:
            if not self.stack1:
                print("Can't dequeue stack is empty")
                return
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            temp = self.stack2[::-1] + self.stack1
            print("Queue (front to rear):", temp)
    
q1 = queue()
q1.enqueue(54)
q1.enqueue(32)
q1.enqueue(1)
q1.enqueue(88)
q1.enqueue(56)
q1.enqueue(76)
q1.dequeue()
q1.dequeue()
q1.enqueue(2)
q1.peek()
print(f"is Queue is empty : {q1.isEmpty()}")
q1.display()

    