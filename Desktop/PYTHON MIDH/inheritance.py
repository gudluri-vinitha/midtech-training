class Animal:

    def eat(self):
        print("Animal eats food")

class Dog(Animal):

    def bark(self):
        print("Dog barks")
dog1 = Dog()
dog1.eat()
dog1.bark()


class Cat(Animal):

    def meow(self):
        print("meowsss")
cat1 = Cat()
cat1.eat()
cat1.meow()



class Pig(Animal):

    def sound(self):
        print("pig sound")
pig1 = Pig()
pig1.eat()
pig1.sound()


class Lion(Animal):

    def lionss(self):
        print("lion sound")
lion1 = Lion()
lion1.eat()
lion1.lionss()


#another example for inheritance
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Result(Student):
    def __init__(self, name, age, marks, result):
        super().__init__(name, age)
        self.marks = marks
        self.result = result

    def details(self):
        print("Name   :", self.name)
        print("Age    :", self.age)
        print("Marks  :", self.marks)
        print("Result :", self.result)

student1 = Result("Ravi", 20, 75, "Pass")

student1.details()