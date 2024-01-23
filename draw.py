class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        print("Creating Line...")
        self.__point1 = p1
        self.__point2 = p2

    def draw(self, canvas, fill_color):
        print(f"Line drawing from ({self.__point1.x},{self.__point1.y}) to ({self.__point2.x},{self.__point2.y})")
        canvas.create_line(self.__point1.x,self.__point1.y,self.__point2.x,self.__point2.y,fill=fill_color,width=2)
class Cell():
    def __init__(self, win=None):
        print("Creating Cell...")
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        print(f"Drawing Cell with corners ({x1},{y1}), ({x2},{y1}), ({x1},{y2}), ({x2},{y2})")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self._win is not None:
            if self.has_left_wall:
                print("Drawing left wall...")
                self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x1, self._y2)),"black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x1, self._y2)),"white")
        if self._win is not None:
            if self.has_top_wall:
                print("Drawing top wall...")
                self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x2, self._y1)),"black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y1),Point(self._x2, self._y1)),"white")
        if self._win is not None:
            if self.has_right_wall:
                print("Drawing right wall...")
                self._win.draw_line(Line(Point(self._x2, self._y1),Point(self._x2, self._y2)),"black")
            else:
                self._win.draw_line(Line(Point(self._x2, self._y1),Point(self._x2, self._y2)),"white")
        if self._win is not None:
            if self.has_bottom_wall:
                print("Drawing bottom wall...")
                self._win.draw_line(Line(Point(self._x1, self._y2),Point(self._x2, self._y2)),"black")
            else:
                self._win.draw_line(Line(Point(self._x1, self._y2),Point(self._x2, self._y2)),"white")

    def draw_move(self, to_cell, undo=False):
        print(f"Drawing move from Cell centred at ({(self._x1+self._x2)//2},{(self._y1+self._y2)//2}) to Cell centred at ({(to_cell._x1+to_cell._x2)//2},{(to_cell._y1+to_cell._y2)//2})")
        if not undo:
            print("New move")
            fill_color = "red"
        else:
            print("Undo move")
            fill_color = "gray"
        self._win.draw_line(Line(Point((self._x1+self._x2)//2,(self._y1+self._y2)//2),Point((to_cell._x1+to_cell._x2)//2,(to_cell._y1+to_cell._y2)//2)),fill_color)

