doors = 100
lst1 = [False]*(doors+1)

for i in range(1, doors+1):
    for j in range(i, 101, i):
        lst1[j] = not lst1[j]

for i in range(len(lst1)):
    if lst1[i]==True:
        print(i, end=" ")