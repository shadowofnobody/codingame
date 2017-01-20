
pi = []
n = int(input())
for i in range(n):
    pi.append(int(input()))
l = len(pi)
tmax = 10000
pi.sort()
mn = 1000
for i in range(len(pi)):
    try:
        if pi[i] > pi[i+1]:
            if pi[i] - pi[i+1] < mn:
                mn = pi[i] - pi[i+1]
        else:
            if pi[i+1] - pi[i] < mn:
                mn = pi[i+1] - pi[i]
    except:
        pass

print(mn)
