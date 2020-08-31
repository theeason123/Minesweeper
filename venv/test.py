from random import randint

bomb_count = 15


def set_grid():
    grid_with_bombs = []
    grid_with_bombs_and_numbers = []

    # create grid with all 0
    grid = [[0 for x in range(30)] for x in range(15)]

    # choose 15 random locations for bombs
    for i in range(bomb_count):
        grid[randint(0, 14)][randint(0, 29)] = 50

    # create a list of bomb locations as tuples
    for c_index, column in enumerate(grid):
        for r_index, row in enumerate(column):
            if row == 50:
                grid_with_bombs.append((c_index, r_index))

    # use tuples from above to mark out any grid cell as next to a bomb
    # and create a temp list of tuples with those locations
    temp_tuple_list = []
    for a, b in grid_with_bombs:

        c = a, b + 1
        d = a, b - 1
        e = a - 1, b - 1
        f = a - 1, b
        g = a - 1, b + 1
        h = a + 1, b - 1
        i = a + 1, b
        j = a + 1, b + 1

        temp_list = [c,d,e,f,g,h,i,j]
        for i in temp_list:
            temp_tuple_list.append(i)

    # now remove tuples that correspond to a grid reference that does not exist. e.g (-1,29)
    for a,b in temp_tuple_list:

        c = a,b
        if a == -1 or a >= 15:
            continue
        if b == -1 or b >= 29:
            continue
        else:
            grid_with_bombs_and_numbers.append(c)


    # every tuple that isnt 50( a bomb ) or 0 ( nothing ) is a number square,
    # each time a tuple is in the list add 1 this will give us a value to display
    for a,b in grid_with_bombs_and_numbers:
        if grid[a][b] != 50:
            grid[a][b] += 1


    return grid


print(set_grid())

# grid = set_bomb_locations()

# grid_with_bombs = number_layout(grid2)
