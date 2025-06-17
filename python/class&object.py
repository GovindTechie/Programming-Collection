class Calculator():
    def __init__(self, n):
        self.n = n

    def squareroot(self):
        print(f"The squreroot of {self.n}: {self.n ** 0.5}")

a = Calculator(64)
a.squareroot()