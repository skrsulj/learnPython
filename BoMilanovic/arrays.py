

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

print("=" * 20)

del a[1][2]

for row in a:
    print(' '.join([str(elem) for elem in row]))



a2 = [1,2,3,4]

print(a2 , len(a2))

del a2[2]

print(a2 , len(a2))
