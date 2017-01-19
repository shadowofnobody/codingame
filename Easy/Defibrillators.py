import math

def myfind(defib, s, x):
    z = 0
    for i in range(len(defib)):
        if defib[i] == s:
            z += 1
        if z == x:
            return(i)

lonA = input(); lonA = lonA.replace(',','.'); lonA = float(lonA)
latA = input(); latA = latA.replace(',','.'); latA = float(latA)
mn = 1000000000

n = int(input())
for i in range(n):
    defib = input()
    defib = defib.replace(',', '.')
    name = defib[myfind(defib, ';', 1)+1:myfind(defib, ';', 2)]
    lonB = defib[myfind(defib, ';', 4)+1:myfind(defib, ';', 5)]; lonB = float(lonB) 
    latB = defib[myfind(defib, ';', 5)+1:]; latB = float(latB)
    x = (lonB - lonA) * math.cos((latA+latB)/2)
    y = (latB - latA)
    d = math.sqrt((x**2) + (y**2)) * 6371
    if d < mn:
        mn = d
        result = name

print (result)
