while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if light_x>initial_tx:
        if light_y>initial_ty:
            print('NE')
        elif light_y<initial_ty:
            print('SE')
        else:
            print('E')
    elif light_x<initial_tx:
        if light_y>initial_ty:
            print('SW')
        elif light_y<initial_ty:
            print('NW')
        else:
            print('W')
    else:
        if light_y<initial_ty:
            print('N')
        elif light_y>initial_ty:
            print('S')