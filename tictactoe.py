def print_grid(grid_input):
    print(' ---------')
    print(' |', grid_input[0], grid_input[1], grid_input[2], '|', sep=' ')
    print(' |', grid_input[3], grid_input[4], grid_input[5], '|', sep=' ')
    print(' |', grid_input[6], grid_input[7], grid_input[8], '|', sep=' ')
    print(' ---------')


xoinput = '         '
print_grid(xoinput)
x_number = 0
o_number = 0
space = 9
three_in_a_row = [[0, 1, 2], [0, 4, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [2, 4, 6], [3, 4, 5], [6, 7, 8]]
row_num = 0
winner = ''
coord = ''
current_player = 'X'

while space != 0:
    input_verified = False
    space_counter = 0
    while input_verified is False:
        coord = input('Enter the coordinates: ')
        if coord[0] not in '1234567890' or coord[2] not in '1234567890':
            print('You should enter numbers!')
        elif coord[0] not in '123' or coord[2] not in '123':
            print('Coordinates should be from 1 to 3!')
        elif xoinput[(int(coord[0]) - 1) * 3 + (int(coord[2]) - 1)].upper() in 'XO':
            print('This cell is occupied! Choose another one!')
        else:
            input_verified = True
    xoinput_update = list(xoinput)
    xoinput_update[(int(coord[0]) - 1) * 3 + (int(coord[2]) - 1)] = current_player
    xoinput = "".join(xoinput_update)
    print_grid(xoinput)
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

    for i in xoinput:
        if i == ' ':
            space_counter += 1
        space = space_counter

    for row in three_in_a_row:  # number of three in a row
        if xoinput[row[0]] == xoinput[row[1]] == xoinput[row[2]]:
            row_num += 1
            winner = xoinput[row[0]]

    if row_num >= 1 and winner != ' ':
        print(winner + ' wins')
        break
    elif space == 0:
        print('Draw')
        break
    else:
        print('Game not finished')
