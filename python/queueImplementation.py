class Queue:
    def __init__(self):
        self.QUEUE_CAPACITY = 101
        self.queue_array = [''] * self.QUEUE_CAPACITY
        self.front_index = 0
        self.rear_index = -1
        self.size = 0

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
            return
        else:
            self.rear_index += 1
            self.queue_array[self.rear_index] = value
            self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            value = self.queue_array[self.front_index]
            self.front_index += 1
            self.size -= 1
            return value

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.QUEUE_CAPACITY

    def peek(self):
        if self.is_empty():
            return None
        return self.queue_array[self.front_index]
