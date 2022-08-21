from tkinter import *
from tkinter.tix import COLUMN, ROW

def Visualization():
    window = Tk()
    window.config(height=300, width=500)
    canvas = Canvas(window,height = 150, width=250, bg='red')
    canvas.place(relx = 0.5, rely = 0.5, anchor= CENTER)
    # button = Button(window,text='button')
    # button.pack()

    playZone =[ [ 0 for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range (3):
            playZone[i][j] = Button(canvas,text='button')
            playZone[i][j].grid(row = i+1, column = j+1)
            # print(playZone)

    window.mainloop()
