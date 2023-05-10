import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guess a number between 1 end {x}: "))
        if guess < random_number:
            print("Sorry, guess again. To Low")
        elif guess > random_number:
            print("Sorry, guess again. To Hight")
    print(f"Correctly number is {random_number}")

guess(10)