from tkinter import *

HEIGHT = 400
WIDTH = 400
window = Tk()
window.title('PLANE WAR')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='green')
c.pack()
window.update()
player_x = 5
player_y = 5
player_id = 0
player_col = "red"
player_lives = 3
player_points = 0
player_speed = 10

#-----------------------------------------------------------------------------------------------------------------------


enemies_rectangle_id = list()
enemies_col = "purple"
enemies_num_in_team = 10


#-----------------------------------------------------------------------------------------------------------------------


bullets = []
bullet_speed = 5
bullet_col = "black"


def create_bullet():
        x, y = get_coords(player_id)
        id1 = c.create_rectangle(x, y, x + 20, y + 10, fill=bullet_col)
        bullets.append(id1)


def move_bullet():
    for i in range(len(bullets)):
        c.move(bullets[i], bullet_speed, 0)


def del_bullet(i):
    c.delete(bullets[i])
    del bullets[i]


def clean_up_bullet():
    for i in range(len(bullets)-1, -1, -1):
        x, y = get_coords(bullets[i])
        if x > 500:
            del_bullet(i)




#-----------------------------------------------------------------------------------------------------------------------



player_id = c.create_polygon(player_x, player_y, 5, 25, 30, 15, fill = player_col)


def move_player(event):
    if event.keysym == 'Up':
        move(0, -1)

    elif event.keysym == 'Down':
        move(0, 1)


c.bind_all('<Key>', move_player)


def move(dx, dy):
    x, y = get_coords(player_id)
    dy_speed = dy * player_speed
    if y + dy_speed > 10 and y + dy_speed < 390:
        c.move(player_id, 0, dy_speed)


def get_coords(id):
    pos = c.coords(id)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

from time import sleep
from random import randint


while True:
    move_bullet()
    if randint(0,100) == 2:
        create_bullet()
    window.update()
    clean_up_bullet()
    print(len(bullets))
    sleep(0.01)



