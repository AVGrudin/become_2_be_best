from tkinter import *


class Square:
    def intersect(self, square):
        return false


class Sprite:
    def __init__(self, x, y):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def event_listener(self, event):
        pass

    def can_go_on(self):
        pass


class Player (Sprite, Square):
    pass


class Door (Sprite, Square):
    def __init__(self, x, y, side, canvas):
        self.id = canvas.create_rectangle(x, y, x + side, y + side)
        self.canvas = canvas

    def can_go_on(self):
        return True


class Wall (Sprite, Square):
    pass




class YouWin(Sprite):
    pass


class Maze:
    def __init__(self, maze_map):
        pass

    def update(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_left(self):
        pass

    def move_right(self):
        pass



maze_map = [[1, 1, 1, 1, 1],[1,'E',0,0,1],[1, 1, 1, 0, 1],[1, 'S', 0, 0, 1],[1, 1, 1, 1, 1]]

HEIGHT = 1000
WIDTH = 1000
window = Tk()
window.title('Bubbles')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='blue')
c.pack()
maze = Maze(window, maze_map, c)


while True:
    pass
