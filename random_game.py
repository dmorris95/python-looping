#Task 1

import random
items = ["knife", "compass", "tape", "bottle", "fork", "rock"]
attempt = 0

while attempt < 50:    
    user_guess = input("Please type an item from the following list: " + ' '.join(items) + ": ")
    if user_guess == random.choice(items):
        print("Congratulations!! You guessed correctly!")
        print("You guessed correctly in " + str(attempt) + " attempts!")
        break
    else:
        print("Your guess was not correct, try again.")
        print("You have guessed " + str(attempt) + " times.")
    attempt += 1