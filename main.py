from window import Window
from draw import Point,Line,Cell
import random

def main():
    win = Window(800, 600)
    random.seed()
    cell_matrix = []
    for i in range(50, 501, 50):
        cell_list = []
        for j in range(150, 601, 50):
            cell = Cell(win)
            cell_list.append(cell)
            cell.has_left_wall = bool(round(random.random()))
            cell.has_top_wall = bool(round(random.random()))
            cell.has_right_wall = bool(round(random.random()))
            cell.has_bottom_wall = bool(round(random.random()))
            cell.draw(j, i, j+50, i+50)
        cell_matrix.append(cell_list)
    for k in range(len(cell_matrix)):
        for l in range(len(cell_matrix[k])):
            if not cell_matrix[k][l].has_left_wall and l != 0 and not cell_matrix[k][l-1].has_right_wall:
                cell_matrix[k][l].draw_move(cell_matrix[k][l-1])
            if not cell_matrix[k][l].has_top_wall and k != 0 and not cell_matrix[k-1][l].has_bottom_wall:
                cell_matrix[k][l].draw_move(cell_matrix[k-1][l])
            if not cell_matrix[k][l].has_right_wall and l != len(cell_matrix[k])-1 and not cell_matrix[k][l+1].has_left_wall:
                cell_matrix[k][l].draw_move(cell_matrix[k][l+1])
            if not cell_matrix[k][l].has_bottom_wall and k != len(cell_matrix)-1 and not cell_matrix[k+1][l].has_top_wall:
                cell_matrix[k][l].draw_move(cell_matrix[k+1][l])
    win.wait_for_close()
main()

