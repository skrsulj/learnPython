#
# Exercise 15
# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
#


def revMe(myList):
    myWords = myList.split(" ")
    revWords = " ".join(reversed(myWords))
    return revWords


text = input("Please enter a sentence : ")

print("Original : " + str(text))
print("Reversed : " + str(revMe(text)))
