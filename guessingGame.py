# This is the guessing game.
import random


secret_number = round(random.random() * 1000)
game_outcome = False

for i in range(10):
    guess = input("Guess a number between 1 and 1,000: ")
    print("You guessed " + guess)
    
    guess_as_int = int(guess)
    if guess_as_int == secret_number:
        print("Congratulations, you guessed the correct number.")
        game_outcome = True
        break
    else:
        if guess_as_int < secret_number:
            print("Your guess was too low. Guess again.")
        else:
            print("Your guess was too high. Guess again.")

if game_outcome == False:
    print("You loser. You do not get to guess again.")
    print("By the way, the number was " + str(secret_number))
