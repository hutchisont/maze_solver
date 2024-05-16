from line import Point, Line
from window import Window


class Cell:
    def __init__(self, window: Window, x1: int, x2: int, y1: int, y2: int):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__window = window
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self, top_left_X: int, top_left_Y: int, bot_right_X: int, bot_right_Y: int):
        if self.has_left_wall:
            bot = Line(Point(top_left_X, top_left_Y),
                       Point(top_left_X, bot_right_Y))
            self.__window.draw_line(bot, "black")

        if self.has_right_wall:
            right = Line(Point(bot_right_X, bot_right_Y),
                         Point(bot_right_X, top_left_Y))
            self.__window.draw_line(right, "black")

        if self.has_top_wall:
            top = Line(Point(top_left_X, top_left_Y),
                       Point(bot_right_X, top_left_Y))
            self.__window.draw_line(top, "black")

        if self.has_bottom_wall:
            bot = Line(Point(top_left_X, bot_right_Y),
                       Point(bot_right_X, bot_right_Y))
            self.__window.draw_line(bot, "black")
