# guessing number game " where the player has to guess a number between 1 and 100. The game continues until  the player guesses the number correctly. The game also keeps track of the number of attempts the player has


from random import randint
import time
# Generate a random number between 1 and 100
number_to_guess = int(randint(1, 100))


def guess_number():
    # Initialize the number of attempts
    attempts = 1
    # Game loop
    while True:
        # Ask the player for their guess
        user_guess = int(input("Guess a number between 1 and 100: "))
        if user_guess <  1 or user_guess > 100:
            print("Please enter a number between 1 and 100")
            attempts += 1

        if user_guess < number_to_guess : 
            print("Too low, try again!")
            attempts += 1

        elif  user_guess > number_to_guess :
            print("Too high, try again!")
            attempts += 1

        elif user_guess is  number_to_guess :
            print(f"Congratulations, you found the number in {attempts} attempts!")
            break

guess_number()