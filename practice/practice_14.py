#
# Exercise 14
# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
#

# using sets
def noDupes(myList):
    myList = set(myList)
    newList = list(myList)
    return newList

# using loop
def noDupes2(myList):
    newList = []
    for item in myList:
        if item not in newList:
            newList.append(item)
    return newList


a = ["Sasa", "Claire", "Fred", "John", "Steve", "Sasa", "Steve"]

print("Original list " + str(a))
print("No Dupes list " + str(noDupes2(a)))
