# Practice 8
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
#
import random

def compare(p1, p2):
    if p1 == p2:
        return "It's a tie"

    if p1 == "R" and p2 == "S":
        return "Player wins"
    elif p1 == "S" and p2 == "P":
        return "Player wins"
    elif p1 == "P" and p2 == "R":
        return "Player wins"
    else:
        return "Computer wins"


while 1:
    player = input("Please enter (R)ock, (P)aper, (S)cissors or (Q)uit : ")

    if player == "Q":
        print("Thank You for playing")
        break
        
    options = ["R", "P", "S"]

    computer = random.choice(options)

    print("Your choice : " + player)
    print("Computer    : " + computer)

    print("Result      : " + compare(player, computer))


