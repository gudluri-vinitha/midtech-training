import random
game=["rock","paper","scissor"]
computer=random.choice(game)
user=input("Enter the choices rock , paper , scissor :")
print("computer:" ,computer)
if user==computer:
    print("it is a tie")
elif user=="rock":
    if computer=="scissor":
        print("you win")
    else:
        print("computer win")  
elif user=="paper":
    if computer=="rock":
        print("you win")
    else:
        print("computer win")  
elif user=="scissor":
    if computer=="paper":
        print("you win")
    else:
        print("computer win")  
else:
    print("invalid response")        



