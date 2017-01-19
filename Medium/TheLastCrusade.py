w, h = [int(i) for i in input().split()]
squares = []
links = {}
for i in range(h):
    line = input()
    squares.append(line.split())
ex = int(input())  

while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    if squares[yi][xi] == '1':
        res = yi + 1, xi 
    elif squares[yi][xi] == '2':
        if pos == 'RIGHT':
            res = yi, xi - 1
        elif pos == 'LEFT':
            res = yi, xi + 1
    elif squares[yi][xi] == '3':
        res = yi + 1, xi
    elif squares[yi][xi] == '4':
        if pos == 'TOP':
            res = yi, xi - 1
        elif pos == 'RIGHT':
            res = yi + 1, xi
    elif squares[yi][xi] == '5':
        if pos == 'TOP':
            res = yi, xi + 1
        elif pos == 'LEFT':
            res = yi + 1, xi
    elif squares[yi][xi] == '6':
        if pos == 'LEFT':
            res = yi, xi + 1
        elif pos == 'RIGHT':
            res = yi, xi - 1
    elif squares[yi][xi] == '7':
        res = yi + 1, xi
    elif squares[yi][xi] == '8':
        res = yi + 1, xi
    elif squares[yi][xi] == '9':
        res = yi + 1, xi
    elif squares[yi][xi] == '10':
        res = yi, xi - 1
    elif squares[yi][xi] == '11':
        res = yi, xi + 1
    elif squares[yi][xi] == '12' or squares[yi][xi] == '13':
        res = yi + 1, xi
    
    
    print(res[1], res[0])
