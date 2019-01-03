#
# Exercise 13
# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
#


def getFib(count):
    fibList = [1,1]
    while len(fibList) <= count:
        newFib = fibList[-2] + fibList[-1]
        fibList.append(newFib)

    return fibList



fibSize = int(input("How many Fibonnaci numbers do you need? : "))

print("Fibonnaci list of " + str(fibSize) + " numbers " + str(getFib(fibSize)))

