from tkinter import *

HEIGHT = 400
WIDTH = 800
window = Tk()
window.title('Квадраты')
c = Canvas(window, width=WIDTH, height=HEIGHT)
c.pack()
c.create_rectangle(0, 0, 400, 400, fill = 'blue')
c.create_rectangle(400, 0, 800, 400, fill = 'red')

while True:
    window.update()
