
l = int(input())
h = int(input())
t = input()
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = t.upper()
for i in range(h):
    row = input()
    res = ""
    
    for j in t:
        if not j in alph:
            res += row[104:108]
        else:
            po = alph.index(j)
            res += row[po*l:(po+1)*l]
    
    print(res)
