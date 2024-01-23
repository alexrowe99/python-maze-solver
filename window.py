from tkinter import Tk, BOTH, Canvas
from draw import Line

class Window():
    def __init__(self, width, height):
        print("Creating Window...")
        self.__root = Tk()
        self.__root.title("Python Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        print("Drawing Window...")
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        print("Closing Window...")
        self.running = False

    def draw_line(self, line, fill_color):
        print("Drawing line to Window...")
        line.draw(self.__canvas, fill_color)

