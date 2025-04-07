import random

valikud = ["rock", "paper", "scissors"]

computer_choice = random.choice(valikud)

print("I have made my chose. Make yours...")
user_choice = input("(rock/paper/scissors): ")

if not user_choice in valikud:
    print("Error: Vale valik")
    exit()

if user_choice == "paper" and computer_choice == "rock" or \
    user_choice == "scissors" and computer_choice == "paper" or \
        user_choice == "rock" and computer_choice == "scissors":
    print("You have won!")
elif user_choice == computer_choice:
    print("Draw!")
else:
    print("Computer has won.")

print("Computer choice was: " + computer_choice)