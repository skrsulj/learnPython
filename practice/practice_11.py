
num = int(input("Please enter a number : "))
divisors = []

for i in range(1,num+1):
    if (num % i) == 0:
        divisors.append(i)

if len(divisors) == 2:
    print(str(num) + " is a prime number")
else:
    print(str(num) + " is not a prime number")


