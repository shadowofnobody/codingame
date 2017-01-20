
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    d_x = ""
    d_y = ""
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if initial_tx < light_x:
        d_x = "E"
        initial_tx += 1
    elif initial_tx > light_x:
        d_x = "W"
        initial_tx -= 1
    if initial_ty < light_y:
        d_y = "S"
        initial_ty += 1
    elif initial_ty > light_y:
        d_y = "N"
        initial_ty -= 1

    print(d_y + d_x)

