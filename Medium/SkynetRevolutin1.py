
n, l, e = [int(i) for i in input().split()]

links = {}
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    try:
        links[n1].append(n2)
    except:
        links[n1] = [n2]
    try:
        links[n2].append(n1)
    except:
        links[n2] = [n1]
    
gates = []    
for i in range(e):
    ei = int(input())  # the index of a gateway node
    gates.append(ei)
    
# game loop
while True:
    si = int(input())   # The index of the node on which the Skynet agent is positioned this turn
    flag = False
    for i in gates:
        if si in links[i]:
            print(si, i)
            flag = True
            break
    if not flag:
        print(si, links[si][0])
