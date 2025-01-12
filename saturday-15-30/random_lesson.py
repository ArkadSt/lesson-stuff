import random
import time
import os
import base64


random_bytes = os.urandom(32)
print(base64.b64encode(random_bytes).decode("utf-8"))

def guess_a_number():
    random_number = random.randrange(100)

    for i in range(7,1,-1):
        user_number = int(input("Enter number (You have {} lives left): ".format(i)))
        if (user_number > random_number):
            print("Your number is too big")
        elif (user_number < random_number):
            print("Your number is too small")
        if (user_number == random_number):
            print("You win!")
            break

def rock_paper_scissors():
    computer_choice = random.choice(["камень", "ножницы", "бумага"])
    user_choice = input("Enter value (камень, ножницы, бумага): ")

    print("Computer choice: " + computer_choice)

    if (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага"):
        print("You win!")
    elif (user_choice == computer_choice):
        print("Draw")
    else:
        print("Computer wins")

#rock_paper_scissors()