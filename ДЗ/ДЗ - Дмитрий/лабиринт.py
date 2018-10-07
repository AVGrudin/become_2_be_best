from tkinter import *


maze = list()
list1 = [1, 1, 1, 1, 1]
list2 = [1, 0, 0, 0, 1]
list3 = [1, 1, 2, 0, 1]
list4 = [1, 10, 0, 0, 1]
list5 = [1, 1, 1, 1, 1]
maze.append(list1)
maze.append(list2)
maze.append(list3)
maze.append(list4)
maze.append(list5)
print(maze)
end = 10
start = 2
wall = 1
position = []
end_position = end

def keyboard_event(event):
    if event.keysym == 'Up':
        new_position = position[1] + 1
        if new_position != wall:
            position = new_position
            if position == end_position:
                print(" we win!!!!!")
    if event.keysym == 'Down':
        new_position = position[1] - 1
        if new_position != wall:
            position = new_position
            if position == end_position:
                print(" we win!!!!!")
    if event.keysym == 'Left':
        new_position = position[2] - 1
        if new_position != wall:
            position = new_position
            if position == end_position:
                print(" we win!!!!!")
    if event.keysym == 'Right':
        new_position = position[2] - 1
        if new_position != wall:
            position = new_position
            if position == end_position:
                print(" we win!!!!!")




for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == start:
            position = [i, j]
            break
print(position)

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] == end:
            end_position = [i, j]
            break
print(position)

square_size = 100/len(maze)

window = Tk()
canvas = Canvas(window, width = 100, height = 100, bg = "blue")
canvas.pack()
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j] != 1:
            canvas.create_rectangle(i*square_size, j*square_size, i*square_size+square_size, j*square_size+square_size, outline="darkgreen", fill="green")

id_gamer = canvas.create_rectangle(position[0]*square_size, position[1]*square_size,
                             (position[0]+1)*square_size, (position[1]+1)*square_size,
                             outline="darkgreen", fill="yellow")

id_door = canvas.create_rectangle(end_position[0]*square_size, end_position[1]*square_size,
                             (end_position[0]+1)*square_size, (end_position[1]+1)*square_size,
                             outline="darkgreen", fill="black")
# по книжке программирование для детей. вам нужно подключить кейборд_евент, чтобы менялась позиция игрока
while True:
    # переместить игрока в новую позицию. и проверить, если игрок на конечной точке, то поменять цвет или размер игрока.
    # вы должны найти ошибки в программе и решить их.
    window.update()

