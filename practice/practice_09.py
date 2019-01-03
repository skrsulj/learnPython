# Practice 9
# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
#
import random

goal = random.randint(1,9)
guess_count = 1

while 1:
    choice = int(input("Please enter a number between 1 and 9 : "))

    if choice < goal:
        print("You guessed low")
    elif choice > goal:
        print("You guessed high")
    else:
        print("You got it")
        break

    guess_count += 1


print("It took " + str(guess_count) + " guesses")
