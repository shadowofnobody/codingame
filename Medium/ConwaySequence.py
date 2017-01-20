n = int(input())
l = int(input())

loop = [str(n)]

for z in range(l-1):
    i = 0
    tloop = []
    while i < len(loop):
        counter = 1
        t = loop[i]
        for j in range(i+1, len(loop)):
            if loop[j] == t:
                counter += 1
            else:
                break
        tloop.append(str(counter))
        tloop.append(str(t))
        i += counter
    loop = tloop
print(' '.join(loop))

