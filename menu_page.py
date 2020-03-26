from tkinter import *
from GUI_Game_plane import *

#Intro Window
intro = Tk()
def destroy():
    intro.destroy()
    free_draw()

intro.title("DEVELOPER")
intro.geometry('800x300')
intro.configure(bg='azure2')
Label(intro,text = 'JAYPEE UNIVERSITY OF ENGINEERING & TECHNOLOGY',font = 'Arial 20 bold',fg = 'Blue',bg='azure2').pack()
Label(intro,text = 'MAZE SOLVER PROJECT',font = 'Arial 20 bold underline',fg = 'Blue',bg='azure2').pack()
Label(intro,text = 'DEVELOPED BY',font = 'Arial',fg = 'Blue',bg='azure2').pack()
Label(intro,text = 'KSHITIZ MISHRA',font = 'Arial',fg = 'Blue',bg='azure2').pack()
Button(intro,text = 'Try Some Maze',font = 'Arial',width=30,bg = 'azure2',relief=SOLID,borderwidth=2,command=destroy).pack(side = BOTTOM)
mainloop()
