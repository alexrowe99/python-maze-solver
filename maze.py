import time
import random
import math
from draw import Cell

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell(self._win)] * self._num_rows for i in range(self._num_cols)]
        
    def _draw_cell(self, i, j):
        self._cells[i][j].draw(self._x1 + i*self._cell_size_x, self._y1 + j*self._cell_size_y, self._x1 + (i+1)*self._cell_size_x, self._y1 + (j+1)*self._cell_size_y)
        if self._win is not None:
            self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_right_wall = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            for col in range(-1,2,2):
                if not i+col < 0 and not i+col >= self._num_cols and not self._cells[i+col][j].visited:
                    to_visit.append((i+col, j, [bool(col+1), bool(col-1)]))
                if not j+col < 0 and not j+col >= self._num_rows and not self._cells[i][j+col].visited:
                    to_visit.append((i, j+col, [bool(col+1), bool(col-1)]))
            if len(to_visit) == 0:
                self._cells[i][j].draw(self._x1 + i*self._cell_size_x, self._y1 + j*self._cell_size_y, self._x1 + (i+1)*self._cell_size_x, self._y1 + (j+1)*self._cell_size_y)
                return
            pick = math.floor(random.random()*len(to_visit))
            if to_visit[pick][0] != i:
                self._cells[i][j].has_right_wall, self._cells[i][j].has_left_wall = to_visit[pick][2]
                self._cells[to_visit[pick][0]][j].has_left_wall, self._cells[to_visit[pick][0]][j].has_right_wall = to_visit[pick][2]
            if to_visit[pick][1] != j:
                self._cells[i][j].has_top_wall, self._cells[i][j].has_bottom_wall = to_visit[pick][2]
                self._cells[to_visit[pick][1]][j].has_bottom_wall, self._cells[to_visit[pick][1]][j].has_top_wall = to_visit[pick][2]
            self._break_walls_r(to_visit[pick][0], to_visit[pick][1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

