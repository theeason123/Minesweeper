import pygame
import sys
from random import randint

#####import images ######

count = 0
bomb = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/bomb.png")
block0 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/clicked_block.png")
block1 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/1_block.png")
block2 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/2_block.png")
block3 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/3_block.png")
block4 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/4_block.png")
block5 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/5_block.png")
block6 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/6_block.png")
block7 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/7_block.png")
block8 = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/8_block.png")
unclickedblock = pygame.image.load("/Users/marceason/PycharmProjects/minesweeper/Minesweeper/Images/unclicked_block.png")


pygame.init()


screensize = width, height = 1000, 800

screen = pygame.display.set_mode(screensize)

s_width = 400
s_height = 600
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 500  # meaning 600 // 20 = 20 height per blo ck
block_size = 30
score = 0
bomb_count = 15

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

test_colors = {50: bomb, 0: block0, 1: block1, 2: block2, 3: block3, 4: block4, 5: block5, 6: block6, 7: block7,
               8: block8, 9: unclickedblock }

list_to_reveal_grid = []

# used to map which blocks should be shown after they have been clicked on
booleangrid = [[True for x in range(30)] for x in range(15)]


def set_grid():
    grid_with_bombs = []
    grid_with_bombs_and_numbers = []

    # create grid with all 0
    grid = [[0 for x in range(30)] for x in range(15)]

    # choose 15 random locations for bombs
    for i in range(bomb_count):
        grid[randint(0, 14)][randint(0, 29)] = 50

    # create a list of bomb locations as tuples
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 50:
                grid_with_bombs.append((i, j))

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
        if b == -1 or b >= 30:
            continue
        else:
            grid_with_bombs_and_numbers.append(c)


    # every tuple that isnt 50( a bomb ) or 0 ( nothing ) is a number square,
    # each time a tuple is in the list add 1 this will give us a value to display
    for a,b in grid_with_bombs_and_numbers:
        if grid[a][b] != 50:
            grid[a][b] += 1


    return grid




def draw_window(grid, bgrid, screen):


    for i in range(len(bgrid)):
        for j in range(len(bgrid[i])):
            if bgrid[i][j]:
                block = screen.blit(test_colors[9], (top_left_x + j * 30, top_left_y + i * 30,))
            else:
                screen.blit(test_colors[grid[i][j]], (top_left_x + j * 30, top_left_y + i * 30,))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if block.collidepoint(pygame.mouse.get_pos()):
                    bgrid[i][j] = False
                    show_empty_blocks(bgrid, grid, i, j)





def show_empty_blocks(boolgrid, block, i, j):

    # unfinished function, is buggy ( doesnt reveal every block as it should )
    # the basic idea of this function was to:
        # 1. test if the block that was selected contains a 0 ( indicating an empty block )
        # 2. reveal every block surrounding the empty block
        # 3. check the  blocks revealed in step 2, if they are 0, reveal every surrounding block.
        # 4. continue steps 2 and 3 until every empty block ( within that part of the grid ) is cleared.
    # NOTE: the above method should also reveal numbered blocks that surround the grid



    tempholding = []
    count = 0

    if block[i][j] == 0:
        tempholding.append((i,j))

        for a,b in tempholding:


            c = a, b + 1
            d = a, b - 1
            e = a - 1, b - 1
            f = a - 1, b
            g = a - 1, b + 1
            h = a + 1, b - 1
            i = a + 1, b
            j = a + 1, b + 1


            all_around_grid = [c,d,e,f,g,h,i,j]

            for item in all_around_grid:
                list_to_reveal_grid.append(item)



        for a,b in list_to_reveal_grid:
            if a == -1 or a >= 15:
                continue
            if b == -1 or b >= 30:
                continue
            else:
                boolgrid[a][b] = False




grid = set_grid()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        draw_window(grid, booleangrid, screen)

        pygame.display.update()
