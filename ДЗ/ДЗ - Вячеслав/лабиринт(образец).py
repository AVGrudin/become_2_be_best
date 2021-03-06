from tkinter import *


def detect_position(num):
  pos = []
  for i in range(len(maze)):
      for j in range(len(maze[i])):
          if maze[i][j] == num:
              pos = [i, j]
              break
  return pos


def detect_end_position():
  return detect_position(end)


def detect_start_position():
  return detect_position(start)


def keyboard_event(event):
    global position
    if event.keysym == 'Up':
        new_x_position = position[0]
        new_y_position = position[1] - 1
        if maze[new_x_position][new_y_position] != wall:
          canvas.move(id_gamer, 0, -square_size)
          position = [new_x_position, new_y_position]

    if event.keysym == 'Down':
        new_x_position = position[0]
        new_y_position = position[1] + 1
        if maze[new_x_position][new_y_position] != wall:
          canvas.move(id_gamer, 0, square_size)
          position = [new_x_position, new_y_position]

    if event.keysym == 'Left':
        new_y_position = position [1]
        new_x_position = position[0] - 1
        if maze[new_x_position][new_y_position] != wall:
            canvas.move(id_gamer, -square_size, 0)
            position = [new_x_position, new_y_position]

    if event.keysym == 'Right':
        new_y_position =position[1]
        new_x_position = position[0] + 1
        if maze[new_x_position][new_y_position] != wall:
            canvas.move(id_gamer, square_size, 0)
            position = [new_x_position, new_y_position]


end_of_game = 0

maze = list()
maze.append([1, 1, 1, 1, 1])
maze.append([1, 2, 0, 0, 1])
maze.append([1, 1, 1, 0, 1])
maze.append([1, 10, 0, 0, 1])
maze.append([1, 1, 1, 1, 1])

print(maze)

end = 10
start = 2
wall = 1
position = []
end_position = []
new_position = []



position = detect_start_position()
end_position = detect_end_position()

maze[position[0]][position[1]] = 0
maze[end_position[0]][end_position[1]] = 0

square_size = 100 / len(maze)



window = Tk()
canvas = Canvas(window, width = 100, height = 100, bg = "blue")
canvas.pack()

way_coords = list()
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == 0:
            id_way = canvas.create_rectangle(i*square_size, j*square_size, i*square_size+square_size, j*square_size+square_size, outline="darkgreen", fill="green")
            way_coords.append(id_way)




id_gamer = canvas.create_rectangle(position[0]*square_size, position[1]*square_size,
                                   (position[0]+1)*square_size, (position[1]+1)*square_size,
                                   outline="darkgreen", fill="yellow")


id_door = canvas.create_rectangle(end_position[0]*square_size, end_position[1]*square_size,
                             (end_position[0]+1)*square_size, (end_position[1]+1)*square_size,
                             outline="darkgreen", fill="black")


canvas.bind_all('<Key>', keyboard_event)

while not (position[0] == end_position[0] and position[1] == end_position[1]):
    window.update()

print("We win!!!!!!")
canvas.itemconfig(id_door, fill = 'darkgreen')

while True:
    window.update()
