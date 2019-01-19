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
    def __init__(self, x, y, side, canvas):
        self.id = canvas.create_rectangle(x, y, x + side, y + side)
        self.canvas = canvas



class YouWin(Sprite):
    pass


class Maze:
    def __init__(self, maze_map, canvas):
        self.walls = []
        for row in range(len(maze_map)):
            for column in range(len(maze_map[row])):
                if maze_map[row][column] == 1:
                    self.walls.append(Wall(250 * row, 250 * column, 250, canvas))
                elif maze_map[row][column] == 'E':
                    self.walls.append(Door(250 * row, 250 * column, 250, canvas))


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
maze = Maze(maze_map, c)


while True:
    window.update()
