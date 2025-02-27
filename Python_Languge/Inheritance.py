class Employee():
    def __init__(self):
        print("this is employee constructor")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("this is programmer constructor")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("this is manager costructor")
    c = 3

o = Manager()
