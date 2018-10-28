maze_halloween = list()
for i in range(10):
    line = []
    for j in range(10):
        line.append(1)
    maze_halloween.append(line)

i = 1
while i < len(maze_halloween) - 1:
    for j in range(len(maze_halloween[0]) - 2):
        maze_halloween[i][j + 1] = 0

    i += 2



i = 2

while i < len(maze_halloween) - 1:
    if i % 4:
        maze_halloween[i][1] = 0
    else:
        maze_halloween[i][len(maze_halloween[i]) - 2] = 0

    i += 2




for line in maze_halloween:
    print(line)