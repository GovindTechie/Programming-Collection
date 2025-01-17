

def decorator(func):
    def dec(*args, **kwargs):
        print("good morning")
        func(*args, **kwargs)
        print("thank you for using this function")
    return dec




# @decorator
def hello():
    print("Hello world")

def add(a, b):
    print(a+b)


hello()
decorator(add)(5, 7)