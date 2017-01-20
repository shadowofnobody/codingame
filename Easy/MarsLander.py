
surface_n = int(input()) 
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
p = 0

# game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if v_speed <= 40 and p < 4:
        p += 1
    else:
        p -= 1

    print(0, p)

