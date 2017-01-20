width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

matrix = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    part = []
    for j in range(width):
        part.append(line[j])
    matrix.append(part)
    
for y1 in range(height):
    for x1 in range(width):
        if matrix[y1][x1] == '0':
            
            for y in range(y1+1, height):
                if matrix[y][x1] == '0':
                    x3 = x1
                    y3 = y
                    break
            else:    
                x3, y3 = (-1, -1)
                
            for x in range(x1+1, width):
                if matrix[y1][x] == '0':
                    x2 = x
                    y2 = y1
                    break
            else:
                x2, y2 = (-1, -1)
                
            print(x1, y1, x2, y2, x3, y3)

