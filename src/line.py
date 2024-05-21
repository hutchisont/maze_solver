from tkinter import Canvas


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x: {self.x}, y: {self.y}"


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"p1: {self.p1}, p2: {self.p2}"

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x,
                           self.p2.y, fill=fill_color, width=2)
