remember = []
number = 0

n = int(input())
tels = {}
for i in range(n):
    telephone = input()
    mytels = tels
    for j in telephone:
        if not j in mytels.keys():
            mytels[j] = {}
            number += 1
        mytels = mytels[j]
    
print(number)

