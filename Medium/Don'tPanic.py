
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
flags = {}
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    flags[elevator_floor] = elevator_pos
    
# game loop
while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    if clone_floor == exit_floor:
        if clone_pos > exit_pos:
            if direction == 'RIGHT':
                print('BLOCK')
            else:
                print('WAIT')
        elif clone_pos < exit_pos:
            if direction == 'LEFT':
                print('BLOCK')
            else:
                print('WAiT')
        else:
            print('WAIT')
    elif clone_floor == -1:
        print('WAIT')
    else:
        if clone_pos > flags[clone_floor]:
            if direction == 'RIGHT':
                print('BLOCK')
            else:
                print('WAIT')
        elif clone_pos < flags[clone_floor]:
            if direction == 'LEFT':
                print('BLOCK')
            else:
                print('WAiT')
        else:
            print('WAIT')
