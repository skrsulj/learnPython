#
# Exercise 12
# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
#


def getEnds(listA):
    newList = []
    newList.append(a[0])
    newList.append(a[-1])
    return newList


a = [5, 10, 15, 20, 25]

b = getEnds(a)

print("Original list  : " + str(a))
print("Processed list : " + str(b))
