class Student:
    def display(self,name):
        print("student name:",name)
s1=Student()    
s2=Student()        
s1.display("ravi")

#class and objects task
#class is nothing but a template used to create objects
class Student:
    def __init__(self,Name,Age,Marks,Result):
        self.Name=Name
        self.Age=Age
        self.Marks=Marks
        self.Result=Result
    def display(self):
        print("Name:" ,self.Name)
        print("Age:" ,self.Age)
        print("Marks:" ,self.Marks)
        print("Result:" ,self.Result)

#creates a object forthe class name,object is nothing but an instance(example )  of class
s=Student("Ravi",20,75,"pass") 
s.display()       
            
