from window import Window
from draw import Point,Line,Cell
import random

def main():
    win = Window(800, 600)
    random.seed()
    cell_matrix = []
    for i in range(150, 601, 50):
        cell_list = []
        for j in range(50, 501, 50):
            cell = Cell(win)
            cell_list.append(cell)
            cell.has_left_wall = bool(round(random.random()))
            cell.has_top_wall = bool(round(random.random()))
            cell.has_right_wall = bool(round(random.random()))
            cell.has_bottom_wall = bool(round(random.random()))
            cell.draw(i, j, i+50, j+50)
    for i in range(len(cell_matrix)):
        for j in range(len(cell_matrix[i])):
            if not cell_matrix[i][j].has_left_wall and i != 0 and not cell_matrix[i-1][j].has_right_wall:
                cell_matrix[i][j].draw_move(cell_matrix[i-1][j])
            if not cell_matrix[i][j].has_top_wall and j != 0 and not cell_matrix[i][j-1].has_bottom_wall:
                cell_matrix[i][j].draw_move(cell_matrix[i][j-1])
            if not cell_matrix[i][j].has_right_wall and i != len(cell_matrix[i])-1 and not cell_matrix[i+1][j].has_left_wall:
                cell_matrix[i][j].draw_move(cell_matrix[i+1][j])
            if not cell_matrix[i][j].has_bottom_wall and j != len(cell_matrix)-1 and not cell_matrix[i][j+1].has_top_wall:
                cell_matrix[i][j].draw_move(cell_matrix[i][j+1])
    win.wait_for_close()

main()

