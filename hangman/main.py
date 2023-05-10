import random
import string
from words import words

def get_valid_word(words):
    word = random(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_latters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_latters = set()

    lives = 6

    while len(word_latters) > 0 and lives > 0:
        print("You have ", lives, " You have used ehese latters: ", " ".join(used_latters))
        word_list = [letter if letter in used_latters else '-' for latter in word]

        used_latters = input("Guess a latter: ").upper()
        if(used_latters in alphabet - used_latters):
            used_latters.add(used_latters)
            if used_latters in word_latters:
                word_latters.remove(used_latters)

            else:
                lives = lives - 1
                print("Letter is not in word.")
        
        elif used_latters in used_latters:
            print("You have already udes that character. Plase try again.")
        
        else:
            print("Invalid character. Plase try again.")

    if(lives == 0):
        print("You died". word)
    else:
        print("You guessed the word", word, "!!")

hangman()