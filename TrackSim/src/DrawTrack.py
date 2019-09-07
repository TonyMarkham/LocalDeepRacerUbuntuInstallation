from graphics import *

def main():
    win = GraphWin("Track Simulation", 800, 600)
    win.setBackground(color_rgb(255, 255, 255))

    point_01 = Point(0, 0)
    point_02 = Point(800, 600)

    line = Line(point_01, point_02)
    line.setWidth(3)
    line.setOutline(color_rgb(0, 0, 0))
    line.draw(win)

    win.getMouse()
    win.close



main()