n = int(input())
x = []
for i in input().split():
    v = int(i)
    x.append(v)
m = 0
ma = max(x)
mi = min(x)
ima = x.index(ma)
imi = x.index(mi)
l = len(x)
if l < 200:
    if ima < imi:
        m = ma - mi
    else:
        for i in range(len(x)-1):
            t = x[i+1:]
            t.sort()
            y = x[i] - t[0]
            if y > m:
                m = y
else:
    for i in range(ima, l):
        t = ma - x[i]
        if t > m:
            m = t
    for i in range(0, imi):
        t = x[i] - mi
        if t > m:
            m = t
        
print(-m)

