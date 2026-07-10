import math

while True:

    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Square (x²)")
    print("7. Cube (x³)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. Log Base 10")
    print("12. Natural Log (ln)")
    print("13. Pi (π)")
    print("14. Euler Number (e)")
    print("15. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer =", a + b)

    elif choice == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer =", a - b)

    elif choice == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer =", a * b)

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Answer =", a / b)

    elif choice == 5:
        a = float(input("Enter number: "))
        print("Square Root =", math.sqrt(a))

    elif choice == 6:
        a = float(input("Enter number: "))
        print("Square =", math.pow(a, 2))

    elif choice == 7:
        a = float(input("Enter number: "))
        print("Cube =", math.pow(a, 3))

    elif choice == 8:
        a = float(input("Enter angle in degrees: "))
        print("Sin =", math.sin(math.radians(a)))

    elif choice == 9:
        a = float(input("Enter angle in degrees: "))
        print("Cos =", math.cos(math.radians(a)))

    elif choice == 10:
        a = float(input("Enter angle in degrees: "))
        print("Tan =", math.tan(math.radians(a)))

    elif choice == 11:
        a = float(input("Enter number: "))
        print("Log =", math.log10(a))

    elif choice == 12:
        a = float(input("Enter number: "))
        print("Natural Log =", math.log(a))

    elif choice == 13:
        print("Pi =", math.pi)

    elif choice == 14:
        print("Euler Number =", math.e)

    elif choice == 15:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")