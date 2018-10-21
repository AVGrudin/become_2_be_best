from tkinter import *



def keyboard_event(event):
    global position2
    if event.keysym == 'Up':
        new_x_position2 = position2[0]
        new_y_position2 = position2[1] - 1
        if maze[new_x_position2][new_y_position2] != wall:
          canvas.move(id_gamer, 0, -square_size)
          position2 = [new_x_position2, new_y_position2]

    elif event.keysym == 'Down':
        new_x_position2 = position2[0]
        new_y_position2 = position2[1] + 1
        if maze[new_x_position2][new_y_position2] != wall:
          canvas.move(id_gamer, 0, square_size)
          position2 = [new_x_position2, new_y_position2]

    elif event.keysym == 'Left':
        new_x_position2 = position2[0] - 1
        new_y_position2 = position2[1]
        if maze[new_x_position2][new_y_position2] != wall:
          canvas.move(id_gamer, -square_size, 0)
          position2 = [new_x_position2, new_y_position2]
    elif event.keysym == 'Right':
        new_x_position2 = position2[0] + 1
        new_y_position2 = position2[1]
        if maze[new_x_position2][new_y_position2] != wall:
            canvas.move(id_gamer, square_size, 0)
            position2 = [new_x_position2, new_y_position2]


def detect_position2(num):
  pos = []
  for i in range(len(maze)):
      for j in range(len(maze[i])):
          if maze[i][j] == num:
              pos = [i, j]
              break
  return pos


def detect_end_position2():
  return detect_position2(end)


def detect_start_position2():
  return detect_position2(start)


maze = list()
maze.append([1, 1, 1, 1, 1])
maze.append([1, 2, 0, 0, 1])
maze.append([1, 1, 0, 1, 1])
maze.append([1, 10, 0, 0, 1])
maze.append([1, 1, 1, 1, 1])


print(maze)

end = 10
start = 2
wall = 1
position2 = []
end_position2 = []
new_position2 = []




position2 = detect_start_position2()
end_position2 = detect_end_position2()

maze[position2[0]][position2[1]] = 0
maze[end_position2[0]][end_position2[1]] = 0

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






id_gamer = canvas.create_rectangle(position2[0]*square_size, position2[1]*square_size,
                                   (position2[0]+1)*square_size, (position2[1]+1)*square_size,
                                   outline="darkgreen", fill="yellow")


id_door = canvas.create_rectangle(end_position2[0]*square_size, end_position2[1]*square_size,
                             (end_position2[0]+1)*square_size, (end_position2[1]+1)*square_size,
                             outline="darkgreen", fill="black")




canvas.bind_all('<Key>', keyboard_event)

while not(position2[0] == end_position2[0] and position2[1] == end_position2[1]):
    window.update()

canvas.itemconfig(id_door, fill = 'darkgreen')
canvas.create_text(50, 50, text="You win!!!!!!", fill='white', )

while True:
    window.update()
