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
from random import randint


enemies = list()
enemies_col = "purple"
enemies_speed = 1

def create_enemy():
    x =390
    y = randint(10,390)
    id2 = c.create_rectangle(x, y, x + 20, y + 10, fill=enemies_col)
    enemies.append(id2)


def move_enemy():
    for i in range(len(enemies)):
        c.move(enemies[i], -enemies_speed, 0)


def del_enemy(i):
    c.delete(enemies[i])
    del enemies[i]

def bullets_destroy_enemies():
    for i in range(len(enemies) - 1, -1, -1):
        for j in range(len(bullets) - 1, -1, -1):
            b_pos = c.coords(bullets[j])
            e_pos = c.coords(enemies[i])
            b_x1 = b_pos[0]
            b_y1 = b_pos[1]
            b_x2 = b_pos[2]
            b_y2 = b_pos[3]
            e_x1 = e_pos[0]
            e_y1 = e_pos[1]
            e_x2 = e_pos[2]
            e_y2 = e_pos[3]
            if b_x2 > e_x1 and e_y1 < b_y2-10 and b_y1 < e_y2 or b_x2 > e_x1 and b_y1< e_y1 and e_y1 < b_y2+10 and b_y1+10 > e_y1 or b_x2 > e_x1 and b_y1 == e_y1 and b_y2 == e_y2:
                del_enemy(i)


def clean_up_enemy():
    for i in range(len(enemies) - 1, -1, -1):
        x, y = get_coords(enemies[i])
        if x < 0:
            del_enemy(i)

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
        if len(enemies) > 0:
            x, y = get_coords(bullets[i])
            if x > 400:
                del_bullet(i)




#-----------------------------------------------------------------------------------------------------------------------



player_id = c.create_polygon(player_x, player_y, 5, 25, 30, 15, fill = player_col)


def move_player_and_boom(event):
    if event.keysym == 'Up':
        move(-1)

    elif event.keysym == 'Down':
        move(1)

    if event.keysym == 'space':
        create_bullet()








c.bind_all('<Key>', move_player_and_boom)


def move(dy):
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
        create_enemy()
    window.update()
    move_enemy()
    clean_up_enemy()
    clean_up_bullet()
    bullets_destroy_enemies()


    sleep(0.01)



