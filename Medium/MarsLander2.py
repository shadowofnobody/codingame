# THANKS TO fabriziocucci's GITHUB FOR THIS SOLUTION

import math

# init data
grav = 3.711
surface_n = int(input())
xmap = []
ymap = []
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    xmap.append(land_x); ymap.append(land_y)
    
# find landing positions
for i in range(len(xmap) - 1):
    if ymap[i] == ymap[i+1]:
        land = (xmap[i], xmap[i+1])
        yh = ymap[i]
        break

# functions
def island(x, land): # checking for flat position
    return (x > land[0]) and (x < land[1])
    
def landing(y, yh): # checking if mars lander is about to land
    return y < yh + 50
    
def speedlimit(h_speed, v_speed): # checking for speed limit
    return (abs(h_speed) <= 15) and (abs(v_speed) <= 35)
    
def SpeedDown(h_speed, v_speed): # Slow up mars lander
    speed = math.sqrt(h_speed ** 2 + v_speed ** 2)
    radians = math.asin(h_speed / speed)
    return math.degrees(radians)
    
def tooFast(h_speed): # checking if mars lander is too fast
    return abs(h_speed) > (20 * 4)

def tooSlow(h_speed): # checking if mars lander is too slow 
    return abs(h_speed) < (20 * 2)
    
def SpeedUp(x, land): # Speed up mars lander to avoid fuel consumption
    if x < land[0]:
        return 0 - math.degrees(math.acos(grav / 4.0))
    if x > land[1]:
        return math.degrees(math.acos(grav / 4.0))
    return 0
    
def power(v_speed):
    if v_speed >= 0: # calculating power
        return 3
    else:
        return 4

def rightdirection(x, h_speed, land): # checking for right direction
    if x > land[1] and h_speed > 0:
        return False
    elif x < land[0] and h_speed < 0:
        return False
    return True

# game loop
while True:
    x, y, h_speed, v_speed, fuel, ang, p = [int(i) for i in input().split()]
    
    if island(x, land): # if mars lander is about to land
        if landing(y, yh):
            ang = 0; p = 3
        elif speedlimit(h_speed, v_speed):
            ang = 0; p = 2
        else:
            ang = SpeedDown(h_speed, v_speed)
            p = 4
    else: # else
        if not rightdirection(x, h_speed, land) or tooFast(h_speed):
            ang = SpeedDown(h_speed, v_speed)
            p = 4
        elif tooSlow(h_speed):
            ang = SpeedUp(x, land)
            p = 4
        else:
            ang = 0
            p = power(v_speed)
    		
    print(int(ang), int(p))
