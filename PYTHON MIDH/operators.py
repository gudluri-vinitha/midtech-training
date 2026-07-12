#arthemetic operator
telugu=98
hindi=99
english=97
maths=100
science=99
social=95
total=telugu+hindi+english+maths+science+social
percentage=(total/600)*100
print("total" ,total)
print("total percentage",percentage)
#assignment operator
a = 10
a -= 3
print("a:",a)

#comparison operators
age=18
if(age>=18):
    print("eligible for vote")
else:
    print("not eligible")
#logical operators
a = 10
b = 20

if a < 15 and b > 15:
    print("True")
else:
    print("False")
#identity operator
a=[1,2]
b=[1,2,3]
print("basic example a is b:",a is b)
#membership operator
students=["sai","siri","sani"]
search_name="siri"
print(search_name, ":is present in", search_name in students)
#bitwise operator
READ = 1
WRITE = 2
EXECUTE = 4

user_permission = READ | WRITE

print("Can read:", bool(user_permission & READ))
print("Can write:", bool(user_permission & WRITE))
print("Can execute:", bool(user_permission & EXECUTE))