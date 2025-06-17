class Employee:
    def __init__(self, name, id):
        self.__name = name
        self.id = id


    def ShowDetail(self):
        print(f"The name of employee {self.id} is {self.name}")


class Programmer(Employee):
    def ShowLanguage(self):
        print("The default language is python")



emp1 = Employee("Ram", 12)
# print(emp1.__dir__())
emp1.ShowDetail()
emp2 = Programmer("Govind", 72)
emp2.ShowLanguage()