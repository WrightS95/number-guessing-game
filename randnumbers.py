import math
import random

computer_choice = random.randint(0, 100)
print(computer_choice)
print("The computer has chosen a random number! Your guess: ")
guess = int(input())


while guess != computer_choice:
    if guess < computer_choice:
        print("Higher!")
        print("Guess: ")
        guess = int(input())
    elif guess > computer_choice:
        print("Lower!")
        print("Guess: ")
        guess = int(input())

if guess == computer_choice:
    print("Correct!")

