from tkinter import *

root = Tk()
canvas_w = 1300
canvas_h = 700
box_g = 50
f = Canvas(root,width=canvas_w,height=50)
f.pack()
w = Canvas(root,width=canvas_w,height=canvas_h)
w.pack()

#w.create_rectangle(row,col,row+box_g,col+box_g)

for row in range(int(canvas_w/box_g)):
    for col in range(int(canvas_h/box_g)):
        w.create_rectangle(row*box_g,col*box_g,row*box_g+box_g,col*box_g+box_g,fill="lightblue")   

mainloop()
