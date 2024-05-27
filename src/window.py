from tkinter import Tk, BOTH, Canvas
from line import Line


class Window:
    def __init__(self, width: int, height: int):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, height=height, width=width, bg="white")
        self.__running = False
        self.canvas.pack()

        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.canvas, fill_color)
