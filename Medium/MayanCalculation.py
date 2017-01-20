# init data
l, h = [int(i) for i in input().split()]
numeral = [''] * 20
for i in range(h):
    numcode = input()
    for j in range(20):
        numeral[j] += numcode[j*l:j*l+l]

# 1 number    
s = int(input())
num_line = ''
num1 = []
for i in range(s):
    num_line += input()
for i in range(0, s, l):
    num1.append(numeral.index(num_line[i*l:i*l+l*h]))
n1 = 0
num1.reverse()
for i in range(s//l):
    n1 += num1[i] * 20 ** i

# 2 number    
s = int(input())
num_line = ''
num2 = []
for i in range(s):
    num_line += input()
for i in range(0, s, l):
    num2.append(numeral.index(num_line[i*l:i*l+l*h]))
n2 = 0
num2.reverse()
for i in range(s//l):
    n2 += num2[i] * 20 ** i

# calculating    
operation = input()
if operation == '+':
    ans = n1 + n2
elif operation == '-':
    ans = n1 - n2
elif operation == '*':
    ans = n1 * n2
else:
    ans = n1 // n2

# transforming
for i in range(1000):
    chk = ans//20**i
    if chk == 0:
        rows = i-1
        break

anslist = []
for i in range(rows, -1, -1):
    t = ans // 20 ** i
    anslist.append(t)
    ans -= t*20**i
   
if anslist == []:
    anslist.append(0)
    
for i in anslist:
    for j in range(h):
        print(numeral[i][l*j:l*j+l])

