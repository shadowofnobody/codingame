
we, he = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
xb, yb = [int(i) for i in input().split()]
hb = 0; wb = 0
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if bomb_dir == 'U':
        he = yb
        yo = hb + (he - hb)//2
        xo = xb
        yb = yo
    elif bomb_dir == 'D':
        hb = yb
        yo = hb + (he - hb)//2
        xo = xb
        yb = yo
    elif bomb_dir == 'R':
        wb = xb
        xo = wb + (we - wb)//2
        yo = yb
        xb = xo
    elif bomb_dir == 'L':
        we = xb
        xo = wb + (we - wb)//2
        yo = yb
        xb = xo
    elif bomb_dir == 'UR':
        he = yb
        yo = hb + (he - hb)//2
        wb = xb
        xo = wb + (we - wb)//2
        xb = xo
        yb = yo
    elif bomb_dir == 'DR':
        hb = yb
        yo = hb + (he - hb)//2
        wb = xb
        xo = wb + (we - wb)//2
        xb = xo
        yb = yo
    elif bomb_dir == 'DL':
        hb = yb
        yo = hb + (he - hb)//2
        we = xb
        xo = wb + (we - wb)//2
        xb = xo
        yb = yo
    elif bomb_dir == 'UL':
        he = yb
        yo = hb + (he - hb)//2
        we = xb
        xo = wb + (we - wb)//2
        xb = xo
        yb = yo
    print(xo, yo)

