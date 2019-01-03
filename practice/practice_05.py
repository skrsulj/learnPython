import random

# static list
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = random.sample(range(1,100),20)
b = random.sample(range(1,100),21)

common = []

for i in a:
    if i in b:
        if i not in common:  # don't import if already in list
            common.append(i)


print("List A : " + str(a))
print("List B : " + str(b))
print("Common : " + str(common))


            
