'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)
'''
import random
how_high= int(input("How high do you want to guess to?"))
num = random.randint(1, how_high)
user_num = int(input("Guess the number: "))

while user_num != num:

    if num > user_num:
        print("You guessed to low!")

    elif num < user_num:
        print("You guessed to high")

    user_num = int(input("Guess again: "))


print("Correct!")

