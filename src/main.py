from cell import Cell
# from line import Point, Line
from window import Window


def main():
    win = Window(800, 600)

    # p1 = Point(100, 500)
    # p2 = Point(200, 200)
    # p3 = Point(300, 300)
    # p4 = Point(600, 500)

    # l1 = Line(p1, p2)
    # l2 = Line(p3, p4)
    #
    # win.draw_line(l1, "black")
    # win.draw_line(l2, "black")

    c1 = Cell(win, 500, 500, 600, 600)
    c1.draw(500, 500, 600, 600)
    c2 = Cell(win, 100, 100, 200, 200)
    c2.has_top_wall = False
    c2.draw(100, 100, 200, 200)
    c3 = Cell(win, 200, 200, 300, 300)
    c3.has_left_wall = False
    c3.has_right_wall = False
    c3.draw(200, 200, 300, 300)
    c4 = Cell(win, 300, 300, 400, 400)
    c4.has_bottom_wall = False
    c4.has_left_wall = False
    c4.draw(300, 300, 400, 400)

    c2.draw_move(c1, True)

    win.wait_for_close()


if __name__ == "__main__":
    main()
