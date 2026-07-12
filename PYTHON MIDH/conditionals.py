a = 10
b = 30
c = 90

# Find maximum of num
if a >= b and a >= c:
    print("Maximum:", a)
elif b >= a and b >= c:
    print("Maximum:", b)
else:
    print("Maximum:", c)

# Find minimum of num

if a <= b and a <= c:
    print("Minimum:", a)
elif b <= a and b <= c:
    print("Minimum:", b)
else:
    print("Minimum:", c)

#if else if condition
marks = int(input("Enter the marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 35:
    print("Grade E")
else:
    print("Fail")

#nested if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("Allowed to vote")
    else:
        print("Citizenship required")
else:
    print("Age must be at least 18")
    