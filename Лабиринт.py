

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

    def event_listener(event)


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
