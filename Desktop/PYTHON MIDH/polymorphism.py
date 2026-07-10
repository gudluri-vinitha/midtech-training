
class Animal:
    def sound(self):
        print("animal makes a sound")
       


class Dog:
    def sound(self):
        print("cat")
       
class Cat:
    def sound(self):
        print("cat meows")
animals=[Animal(),Dog(),Cat()]   
for animal in animals:
    animal.sound()  

def add(a,b=0,c=0):
    return a+b+c

print("add(5):",add(5))       
print("add(5,10):",add(5,10))       
print("add(5,10,15):",add(5,10,15))       


#another task for polymorphism


class Student:
    def details(self):
        print("Name   : Ravi")
        print("Age    : 20")

class Result:
    def details(self):
        print("Marks  : 75")
        print("Result : Pass")


student1 = Student()
student2 = Result()
student1.details()

student2.details()
        
        
       










