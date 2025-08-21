class MinStack(object):

    def __init__(self):
        self.stack = []
        self.MinStack = []
        

    def push(self, val):
        self.stack.append(val)
        if(not self.MinStack or self.MinStack[-1] != self.stack[-1]) :
            self.MinStack.append(val)
        else:
            self.MinStack.append(self.MinStack[-1])

    def pop(self):
        self.stack.pop()
        self.MinStack.pop()

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.MinStack[-1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
# obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()