from consts import *
import game_field


def create_knight_grid():
    return [[(i, j) for j in range(KNIGHT_COL)] for i in range(KNIGHT_ROW)]


def right(knight):
    new_one = knight[0][1][1]
    if new_one < NUM_OF_COLS:
        for i in range(KNIGHT_ROW):
            for j in range(KNIGHT_COL):
                new = int(knight[i][j][1])+1
                knight[i][j] = (knight[i][j][0], new)
    return knight


def left(knight):
    new_one = knight[0][1][1]
    if new_one > 0:
        for i in range(KNIGHT_ROW):
            for j in range(KNIGHT_COL):
                new=int(knight[i][j][1])-1
                knight[i][j]= (knight[i][j][0],new)
    return knight


def up(knight):
    new_one = knight[0][1][0]
    if new_one < NUM_OF_ROWS:
        for i in range(KNIGHT_ROW):
            for j in range(KNIGHT_COL):
                new=int(knight[i][j][1])+1
                knight[i][j]= (new,knight[i][j][0])
    return knight


def down(knight):
    new_one = knight[0][1][0]
    if new_one < NUM_OF_ROWS:
        for i in range(KNIGHT_ROW):
            for j in range(KNIGHT_COL):
                new=int(knight[i][j][1])-1
                knight[i][j]= (new,knight[i][j][0])
    return knight


'''def hit_landmine():
    #return True if legs hit landmine
    pass


def get_knight_pos(knight):
    #return the left corner of knight's position
    return tuple([game_field.calc_col(knight[0][1]), game_field.calc_row(knight[0][0])])'''


knight=create_knight_grid()
knight=right(knight)
knight=left(knight)
knight=up(knight)
knight=down(knight)

