from window import Window
from line import Point, Line


def main():
    win = Window(800, 600)

    p1 = Point(100, 500)
    p2 = Point(200, 200)
    p3 = Point(300, 300)
    p4 = Point(600, 500)

    l1 = Line(p1, p2)
    l2 = Line(p3, p4)

    win.draw_line(l1, "black")
    win.draw_line(l2, "black")

    win.wait_for_close()


if __name__ == "__main__":
    main()
