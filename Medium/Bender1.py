# creating map
l, c = [int(i) for i in input().split()]
gmap = []
for i in range(l):
    row = input()
    gmap.append(row)

# init pos for Bender and T coordinates
t1 = ''
t2 = ''
for i in range(len(gmap)):
    for j in range(len(gmap[i])):
        if gmap[i][j] == '@':
            pos = (i, j)
        elif gmap[i][j] == 'T':
            if t1 == '':
                t1 = (i, j)
            else:
                t2 = (i, j)

# init data
course = ['SOUTH', 'EAST', 'NORTH', 'WEST']
allow = [' ', 'I', 'T', 'B', 'E', 'S', 'N', 'W', '$']
steps = []
step = 'SOUTH'
bmode = False
z = 0

# game loop
while True:
    # next pos
    z += 1
    if z >= 200:
        print('LOOP')
        break
    if step == 'SOUTH':
        npos = (pos[0] + 1, pos[1])
    elif step == 'NORTH':
        npos = (pos[0] - 1, pos[1])
    elif step == 'EAST':
        npos = (pos[0], pos[1] + 1)
    elif step == 'WEST':
        npos = (pos[0], pos[1] - 1)
        
    # cheking npos object
    if gmap[npos[0]][npos[1]] == ' ': # empty
        pos = npos
        steps.append(step)
    elif gmap[npos[0]][npos[1]] == '#': # # obstacle
        for i in course:
            if i == 'SOUTH':
                if gmap[pos[0] + 1][pos[1]] in allow:
                    step = 'SOUTH'
                    break
            elif i == 'EAST':
                if gmap[pos[0]][pos[1] + 1] in allow:
                    step = 'EAST'
                    break
            elif i == 'NORTH':
                if gmap[pos[0] - 1][pos[1]] in allow:
                    step = 'NORTH'
                    break
            elif i == 'WEST':
                if gmap[pos[0]][pos[1] - 1] in allow:
                    step = 'WEST'
                    break
        continue
                
        steps.append(step)
    elif gmap[npos[0]][npos[1]] == 'I': # inverter
        pos = npos
        course.reverse()
        steps.append(step)
    elif gmap[npos[0]][npos[1]] == 'B': # beer
        pos = npos
        if bmode == False:
            bmode = True
            allow.append('X')
        else:
            bmode = False
            allow.pop()
        steps.append(step)
    elif gmap[npos[0]][npos[1]] == 'X': # X obstacle
        if bmode == True:
            pos = npos
            gmap[pos[0]] = gmap[pos[0]][:pos[1]] + ' ' + gmap[pos[0]][pos[1]+1:]
            steps.append(step)
        else:
            for i in course:
                if i == 'SOUTH':
                    if gmap[pos[0] + 1][pos[1]] in allow:
                        step = 'SOUTH'
                        break
                elif i == 'EAST':
                    if gmap[pos[0]][pos[1] + 1] in allow:
                        step = 'EAST'
                        break
                elif i == 'NORTH':
                    if gmap[pos[0] - 1][pos[1]] in allow:
                        step = 'NORTH'
                        break
                elif i == 'WEST':
                    if gmap[pos[0]][pos[1] - 1] in allow:
                        step = 'WEST'
                        break
            continue
    elif gmap[npos[0]][npos[1]] == 'E': # EAST
        pos = npos
        steps.append(step) 
        step = 'EAST'
    elif gmap[npos[0]][npos[1]] == 'S': # SOUTH
        pos = npos
        steps.append(step)   
        step = 'SOUTH'
    elif gmap[npos[0]][npos[1]] == 'N': # NORTH
        pos = npos
        steps.append(step)   
        step = 'NORTH'
    elif gmap[npos[0]][npos[1]] == 'W': # WEST
        pos = npos
        steps.append(step)
        step = 'WEST'
    elif gmap[npos[0]][npos[1]] == 'T': # teleport
        if npos == t1:
            pos = t2
        else:
            pos = t1
        steps.append(step)
    elif gmap[npos[0]][npos[1]] == '$': # suicide-box
        steps.append(step)
        break

if z < 200:
    for i in steps:
        print(i)
