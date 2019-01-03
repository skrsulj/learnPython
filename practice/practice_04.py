
num = int(input("Please enter a number : "))
divisors = []

for i in range(1,num+1):
    if (num % i) == 0:
        divisors.append(i)

print(str(num) + " has following divisors : " + str(len(divisors)))


