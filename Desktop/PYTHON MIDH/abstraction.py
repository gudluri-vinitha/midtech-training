from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car starts with a key")


# Create object
car1 = Car()

# Call method
car1.start()


#another example for abstraction

from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def details(self):
        pass

class StudentInfo(Student):

    def __init__(self, name, age, marks, result):
        self.name = name
        self.age = age
        self.marks = marks
        self.result = result

    def details(self):
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Marks  :", self.marks)
        print("Result :", self.result)

student1 = StudentInfo("Ravi", 20, 75, "Pass")

student1.details()