#Write a function that takes no arguments
#When run, the function chooses a random integer between 0 and 100
#Ask the user to guess the number chosen
#Return - Too High, Too low, Just right
#Exit the program if correct
#Only exit when the user guesses correctly
#Additional - only give the user 3 chances
#Additional - let the user select the parameters

import random

def guessing_game(start,finish):

    comp_guess = random.randint(start,finish)
    guess_count = 0
    while True:
        if guess_count == 3:
            print(f"You're out of guesses! The number was {comp_guess}")
            break
        user_guess = int(input(f"Guess a number between {start} and {finish}: "))
        if user_guess < comp_guess:
            print(f"{user_guess} is too low!")
            guess_count += 1
        elif user_guess > comp_guess:
            print(f"{user_guess} is too high!")
            guess_count +=1
        else:
            print(f"Correct! {user_guess} was right!")
            break

guessing_game(int(input("Pick a low number: ")),int(input("Pick a high number: ")))


