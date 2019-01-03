import time

year_now = int(time.strftime("%Y"))

name = input("What is your name : ")

age = int(input("How old are you? : "))

year_100 = year_now + (100 - age)

for i in range(age):
    print(str(i) + " : Your name is " + name + " and you'll be 100 in year " + str(year_100))
