
# game loop
while True:
    mh = 0
    ma = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain.
        if mountain_h > mh:
            ma = i
            mh = mountain_h
            
    print(ma)

