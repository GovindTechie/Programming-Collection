class MyQueue(object):

    def __init__(self):
        self.queue = []
        self.FrontIndex = 0

    def enqueue(self, data):
        self.queue.append(data)
        print(f"{data} enqueued to queue")

    def isEmpty(self):
        return self.FrontIndex >= len(self.queue)
    
    def dequeue(self):
        if(self.isEmpty()):
            print(f"Stack is empty can't dequeue")
            return
        print(f"The {self.queue[self.FrontIndex]} is dequed")
        (self.FrontIndex)+=1

    def peek(self):
        if(self.isEmpty()):
            print(f"Stack is empty can't dequeue")
            return
        print(f"The First element is {self.FrontIndex}")

    def display(self):
        if (self.isEmpty()):
            print("Queue is empty")
        else:
            print("Queue (front to rear):", self.queue[(self.FrontIndex):])

q1 = MyQueue()
q1.enqueue(43)
q1.enqueue(23)
q1.enqueue(90)
q1.enqueue(55)
q1.dequeue()
q1.peek()
q1.display()

    
       
















    # def push(self, x):
    #     self.stack1.append(x)
        

    # def pop(self):
        
        

    # def peek(self):
    #     """
    #     :rtype: int
    #     """
        

    # def empty(self):
    #     """
    #     :rtype: bool
    #     """
        
