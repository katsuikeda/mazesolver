from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(200, 200, 300, 300)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(225, 225, 275, 275)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(400, 400, 500, 500)

    win.wait_for_close()


main()
