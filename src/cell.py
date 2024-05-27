from line import Point, Line
from window import Window

color_black = "black"
color_red = "red"
color_gray = "gray"
color_white = "white"


class Cell:
    def __init__(self, window: Window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__window = window
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None

        self.visited = False

    def __repr__(self):
        return f"""has left: {self.has_left_wall}
has right: {self.has_right_wall}
has top: {self.has_top_wall}
has bottom: {self.has_bottom_wall}
x1: {self.__x1}
x2: {self.__x2}
y1: {self.__y1}
y2: {self.__y2}
visited: {self.visited}"""

    def draw(self, top_left_X: int, top_left_Y: int, bot_right_X: int, bot_right_Y: int):
        self.__x1 = top_left_X
        self.__y1 = top_left_Y
        self.__x2 = bot_right_X
        self.__y2 = bot_right_Y

        left = Line(Point(top_left_X, top_left_Y),
                    Point(top_left_X, bot_right_Y))
        color = color_black if self.has_left_wall else color_white
        self.__window.draw_line(left, color)

        right = Line(Point(bot_right_X, bot_right_Y),
                     Point(bot_right_X, top_left_Y))
        color = color_black if self.has_right_wall else color_white
        self.__window.draw_line(right, color)

        top = Line(Point(top_left_X, top_left_Y),
                   Point(bot_right_X, top_left_Y))
        color = color_black if self.has_top_wall else color_white
        self.__window.draw_line(top, color)

        bot = Line(Point(top_left_X, bot_right_Y),
                   Point(bot_right_X, bot_right_Y))
        color = color_black if self.has_bottom_wall else color_white
        self.__window.draw_line(bot, color)

    def get_center_point(self) -> Point:
        center_x = 0
        center_y = 0
        if self.__x1 < self.__x2:
            center_x = self.__x1 + ((self.__x2 - self.__x1) / 2)
        else:
            center_x = self.__x2 + ((self.__x1 - self.__x2) / 2)

        if self.__y1 < self.__y2:
            center_y = self.__y1 + ((self.__y2 - self.__y1) / 2)
        else:
            center_y = self.__y2 + ((self.__y1 - self.__y2) / 2)

        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        color = color_gray
        if undo:
            color = color_red

        my_center = self.get_center_point()
        other_center = to_cell.get_center_point()
        self.__window.draw_line(Line(my_center, other_center), color)
