
HEIGHT = 10
WIDTH = 10
maze_halloween = list()
for i in range(HEIGHT):
    line = []
    for j in range(WIDTH):
        line.append(1)
    maze_halloween.append(line)

num = 2
while True:
    for i in range(3):
        if num > WIDTH:
            break
        maze_halloween[1][num - 1] = 0
        num = num + 1
    num = num + 1
    if num + 1 > WIDTH:
        break




num = 1

num = 4
while True:
    for i in range(3):
        if num > WIDTH:
            break
        maze_halloween[len(maze_halloween) - 2][num - 1] = 0
        num = num + 1
    num = num + 1
    if num + 1 > WIDTH:
        break

num = 2
num2 = 2
while True:
    if num2 > len(maze_halloween) - 3:
        break
    for i in range(1):
        if num > WIDTH:
            break
        maze_halloween[num2][num - 1] = 0
        num = num + 1
    num = num + 1
    if num > WIDTH:
        num = 2
        num2 += 1
        continue















































































for i in range(len(maze_halloween)):
    print(maze_halloween[i])
