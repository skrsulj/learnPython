
num = int(input("Please enter a number : "))
check = int(input("Divide by : "))


if (num % check):
    print(str(num) + " does not divide evenly by " + str(check))
else:
    print(str(num) + " divides by " + str(check))
