class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.__point1 = p1
        self.__point2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.__point1.x,self.__point1.y,self.__point2.x,self.__point2.y,fill=fill_color,width=2)
        canvas.pack()

class Cell():
    def __init__(self, win):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
    
    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1),Point(x1, y2)),"black")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1),Point(x2, y1)),"black")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1),Point(x2, y2)),"black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2),Point(x2, y2)),"black")

    def draw_move(self, to_cell, undo=False):
        if not undo:
            fill_color = "red"
        else:
            fill_color = "gray"
        self._win.draw_line(Line(Point((self._x1+self._x2)//2,(self._y1+self._y2)//2),Point((to_cell._x1+to_cell._x2)//2,(to_cell._y1+to_cell._y2)//2)),fill_color)
