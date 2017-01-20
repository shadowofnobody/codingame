
n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

temps = temps.split(' ')
m = -1000000
mi = '0'
if n == 0:
    pass
else:
    for i in temps:
        if 0 - abs(int(i)) > m:
            mi = i
            m = 0 - abs(int(i))
        elif 0 - abs(int(i)) == m:
            if int(i) < 0:
                pass
            else:
                mi = i
print(mi)

