from tkinter import *
import time

# # TODO: Нужно сделать методы класса Circle, заменить Circle на Circle.
# Также сделать и то, чтобы выводились круги, а не квадраты





class Circle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def intersects(self, Circle):
        # при условии, что игрок всегда перемещается на длину своей стороны
        # все объекты (стены, двери, игрок) находятся в матрице
        return self.x == Circle.x and self.y == Circle.y

    def above_Circle(self):
        return Circle(self.x, self.y - self.size, self.size)

    def under_Circle(self):
        return Circle(self.x, self.y + self.size, self.size)

    def right_Circle(self):
        return Circle(self.x + self.size, self.y, self.size)

    def left_Circle(self):
        return Circle(self.x - self.size, self.y, self.size)


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

    def can_go_on(self):
        return True


class Player (Sprite, Circle):
    def __init__(self, x, y, side, maze, canvas):
        Circle.__init__(self, x, y, side)
        self.id = canvas.create_oval(x, y, x + side, y + side, fill="yellow")
        self.canvas = canvas
        self.maze = maze

    def move_up(self):
        if self.maze.is_empty_cell(self.above_Circle()):
            self.y = self.above_Circle().y
            self.canvas.move(self.id, 0, -self.size)

    def move_down(self):
        if self.maze.is_empty_cell(self.under_Circle()):
            self.y = self.under_Circle().y
            self.canvas.move(self.id, 0, self.size)

    def move_left(self):
        if self.maze.is_empty_cell(self.left_Circle()):
            self.x = self.left_Circle().x
            self.canvas.move(self.id, -self.size, 0)

    def move_right(self):
        if self.maze.is_empty_cell(self.right_Circle()):
            self.x = self.right_Circle().x
            self.canvas.move(self.id, self.size, 0)


class Door (Sprite, Circle):
    def __init__(self, x, y, side, canvas):
        Circle.__init__(self, x, y, side)
        self.id_circle = canvas.create_oval(x, y, x+ side, y + side, fill = "grey")
        self.canvas = canvas

    def __del__(self):
        self.canvas.delete(self.id_squre)
        self.canvas.delete(self.id_circle)

    def can_go_on(self):
        return True


class Wall (Sprite, Circle):
    def __init__(self, x, y, side, canvas):
        Circle.__init__(self, x, y, side)
        self.id = c.create_oval(x, y, x + side, y + side, fill="green")
        self.canvas = canvas

    #def __del__(self):
    #    self.canvas.delete(self.id)

    def can_go_on(self):
        return False


class YouWin(Sprite):
    def __init__(self, canvas):
        self.width = canvas.winfo_width()
        self.height = canvas.winfo_height()
        self.canvas = canvas
        self.id = self.canvas.create_text(0, 0, font=("Purisa", 42), text="You Win!!!", anchor="nw", fill="yellow")
        coords = self.canvas.bbox(self.id)
        xOffset = (self.width / 2) - ((coords[2] - coords[0]) / 2)
        yOffset = (self.height / 2) - ((coords[3] - coords[1]) / 2)
        self.canvas.move(self.id, xOffset, yOffset)
        # если не понимаете что происходит, начните смотреть на значения и результаты вычислений
        # print(xOffset, yOffset, self.width, self.height)

    def __del__(self):
        self.canvas.delete(self.id)


class Maze:
    def __init__(self, maze_map, canvas):
        self.walls = []
        self.door = None
        for row in range(len(maze_map)):
            for column in range(len(maze_map[row])):
                if maze_map[row][column] == 1:
                    self.walls.append(Wall(20 * column, 20 * row, 20, canvas = canvas))
                elif maze_map[row][column] == 'E':
                    self.door = Door(20 * column, 20 * row, 20, canvas = canvas)

    def __del__(self):
        del self.walls

    def update(self):
        pass

    def is_empty_cell(self, Circle):
        for wall in self.walls:
            if wall.intersects(Circle): return wall.can_go_on()
        return True

    def stays_on_door(self, Circle):
        return self.door.intersects(Circle)


def getPlayerPos(maze_map):
    for row in range(len(maze_map)):
        for column in range(len(maze_map[row])):
            if maze_map[row][column] == "S":
                return row, column



maze_map = [[1, 1, 1, 1, 1],
            [1,'E', 0, 0, 1],
            [1, 1, 1, 0, 1],
            [1, 'S', 0, 0, 1],
            [1, 1, 1, 1, 1]]

HEIGHT = 200
WIDTH = 200
window = Tk()
window.title('Bubbles')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='blue')
c.pack()
# для корректного получения параметров canvas необходимо обновить окно
window.update()

maze = Maze(maze_map, c)

x, y = getPlayerPos(maze_map)
player = Player(y * 20, x * 20, 20, maze, c)

window.bind('<Left>', lambda event: player.move_left())
window.bind('<Right>', lambda event: player.move_right())
window.bind('<Up>', lambda event: player.move_up())
window.bind('<Down>', lambda event: player.move_down())

#youwin = YouWin(c)

while not maze.stays_on_door(player):
    window.update()

youwin = YouWin(c)
window.update()
time.sleep(10)
