
compare = int(input("List numbers less then : "))
aList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
bList = []


for i in aList:
    if i < compare:
        #print(str(i) + " is less than " + str(compare))
        bList.append(i)

print("less than " + str(compare) + " : " + str(bList))
