# THANKS FOR IDEA OF SOLUTION TO MISILA'S GITHUB

# init data
n = int(input())
absx = []; ordy = []
x, y = [int(j) for j in input().split()]
maX = x
miX = x
avgY = y
absx.append(x); ordy.append(y)
for i in range(1, n):
    x, y = [int(j) for j in input().split()]
    absx.append(x); ordy.append(y)
    avgY += ordy[i]
    tx = absx[i]
    if tx > maX:
        maX = tx
    elif tx < miX:
        miX = tx
    
# solution    
avgY = avgY / n
cable = maX - miX

sortordy = sorted(ordy)
med = sortordy[int(len(sortordy)/2)]

for i in ordy:
    cable += abs(i - med)


# answer
print(cable)

