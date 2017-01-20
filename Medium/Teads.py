# THANKS TO MISILA'S GITHUB FOR NICE SOLUTION

# init graph
nodes = {}
n = int(input())
for i in range(n):
    xi, yi = [int(j) for j in input().split()]
    if not xi in nodes:
        nodes[xi] = [yi]
    else:
        nodes[xi].append(yi)
    if not yi in nodes:
        nodes[yi] = [xi]
    else:
        nodes[yi].append(xi)

affect = {}
for i in nodes:
  affect[i] = len(nodes[i])
        
# solution
ans = 0

while len(affect) > 2:
    leaves = [i for i, j in affect.items() if j == 1]
    for item in leaves:    
        myelem = nodes[item]
        for x in myelem:
            if x in affect:
                affect[x] -= 1
        del affect[item]
    ans += 1
    

if len(affect) == 2:
    ans += 1
print(ans)

