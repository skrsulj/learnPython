import random

print("Welcome to the DICE game.")

minNumber = 1
maxNumber = 6

playing = True

while playing:
    
    die1 = random.randint(minNumber, maxNumber)
    die2 = random.randint(minNumber, maxNumber)

    message = "You have rolled {0} and {1}"
    print(message.format(die1, die2))

    print("What would you like to do (r=roll again, q=quit)")
    line = input()

    command = line[:1]

    if command == "q":
        playing = False
