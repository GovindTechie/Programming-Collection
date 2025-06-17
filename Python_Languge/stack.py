class Stack:
    def __init__(self):
        self.STACK_CAPACITY = 101
        self.stack_array = [''] * self.STACK_CAPACITY
        self.top_index = -1

    def push(self, character):
        if(self.is_full()):
            print("Stack is full")
            return 
        else :
            self.top_index += 1
            self.stack_array[self.top_index] = character
        
    
    def pop(self):
        if(self.is_empty()):
            print("Stack is empty")
            return None
        else :
            elementRet = self.stack_array[self.top_index]
            self.top_index -= 1
            return elementRet
        
    
    def is_empty(self):
        return self.top_index == -1

    def is_full(self):
        return self.top_index >= self.STACK_CAPACITY - 1

if __name__ == "__main__":
    input_string = "Hello, World!"
    input_length = len(input_string)

    char_stack = Stack()

    # Push each character onto the stack
    for i in range(input_length):
        current_char = input_string[i]
        char_stack.push(current_char)

    # Pop the characters from the stack to construct the reversed string
    reversed_string = ""
    while not char_stack.is_empty():
        reversed_string += char_stack.pop()

    print(reversed_string)
