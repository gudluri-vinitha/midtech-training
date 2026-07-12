import random

number = random.randint(1, 5)

guess = int(input("Enter a number (1 to 5): "))

if guess == number:
    print("You Win!")
else:
    print("You Lose!")
    print("Number was:", number)