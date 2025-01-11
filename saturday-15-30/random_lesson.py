import random
import time
import os
import base64


#random_bytes = os.urandom(32)
#print(base64.b64encode(random_bytes).decode("utf-8"))

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