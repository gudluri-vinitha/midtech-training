#function
def hello():
    print("how are u")
hello()    
hello()
#function task -prime number
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if number <= 1:
    print("Not Prime")
elif is_prime(number):
    print("Prime")
else:
    print("Not Prime")
#parameter function    
def student_details(name,course):

    print("student name:",name)
    print("course :",course)
     

student_details("sai","BA")
student_details("siri","Btech")
#function task-addition,sub,multi
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def mod(a, b):
    return a % b

print("Addition:", add(3, 2))
print("Subtraction:", sub(3, 2))
print("Multiplication:", mul(3, 2))
print("Modulus:", mod(3, 2))

#task 3-without using a parameter in prime number

def is_prime():
    num = int(input("Enter a number: "))

    if num <= 1:
        print("Not Prime")
        return

    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            return

    print("Prime")

is_prime()