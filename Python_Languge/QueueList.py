class Queue:
    def __init__(self):
        self.queue = []

    def enque(self, item):
        self.queue.append(item)

    def deque(self):
        if not self.isEmpty():
            return self.queue.pop()
        else:
            return "Queue is empty, can't deque"
        
    def front(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
    

q = Queue()
q.enque(10)
q.enque(15)
q.enque(30)

print(q.queue)

print(q.deque())
print(q.front())
print(q.isEmpty())
print(q.deque())
print(q.deque())
print(q.deque())
