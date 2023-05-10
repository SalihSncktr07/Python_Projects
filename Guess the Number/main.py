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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correctly(C)?")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f"Computer guessed your number, {guess}")

computer_guess(10)