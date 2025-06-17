class Student:
    def __init__(self, name, rollNo, age):
        self.name = name
        self._rollNo = rollNo
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age>35:
            print("Invalind age given.. age should be less than 35.")
        else:
            self.__age = age


s1 = Student("Govind", 73, 21)
print(s1.get_age())

s1.set_age(34)

print(s1.get_age())