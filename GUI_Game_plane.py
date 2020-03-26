from tkinter import *

def free_draw():
    root = Tk()
    canvas_w = 1300            # canvas width
    canvas_h = 700             # canvas height
    box_g = 50                 # width of each rectangle
    detination_points = []     # list of start and end point
    barries_points = []        # obstacals where path not exist
    mat_size = []              # matrix size
    uid = []                   # unique id of each cell

    def shortest(k):
        R,C=mat_size[0][0],mat_size[0][1]
        start,end=detination_points[0],k
        r,c=start[0],start[1]
        visited = [(r,c)]
        dr = [-1, +1, 0, 0]
        dc = [ 0, 0, +1, -1]
        for r,c in visited:
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                # C for the number of rows and columns
                if rr < 0 or cc < 0: continue        # Skip invalid cells
                if rr >= R+1 or cc >= C+1: continue  # Skip invalid cells
                if (((rr,cc) not in visited) and ((rr,cc) not in barries_points)) :
                    visited.append((rr,cc))
                    i = uid[rr + cc*(R+1)]
                    can.itemconfig(i,fill="bisque")
                #(rr, cc) neighbouring cell (r,c)
                #(rr, cc) neighbouring cell (r,c)
                if (rr == end[0]) and (cc == end[1]):
                    i = uid[ rr + cc*(R+1)]
                    can.itemconfig(i,fill="green")    
                    if (r,c) == visited[0]:
                        return
                    else:
                        shortest((r,c))   #recursively call the function
                        return


    def search():
        R,C=mat_size[0][0],mat_size[0][1]
        start,end=detination_points[0],detination_points[1]
        r,c=start[0],start[1]   # starting point
        visited = [(r,c)]
        dr = [-1, +1, 0, 0]
        dc = [ 0, 0, +1, -1]
        
        for r,c in visited:
            for i in range(4):
                rr = r + dr[i]
                cc = c + dc[i]
                # C for the number of rows and columns
                if rr < 0 or cc < 0: continue        # Skip invalid cells
                if rr >= R+1 or cc >= C+1: continue  # Skip invalid cells
                if (((rr,cc) not in visited) and ((rr,cc) not in barries_points)) :
                    visited.append((rr,cc))
                    i = uid[rr + cc*(R+1)]
                    can.itemconfig(i,fill="bisque")
                #(rr, cc) neighbouring cell (r,c)
                #(rr, cc) neighbouring cell (r,c)
                if (rr == end[0]) and (cc == end[1]):
                    i = uid[ rr + cc*(R+1)]
                    can.itemconfig(i,fill="red")    
                    if (r,c) == visited[0]:
                        return
                    else:
                        shortest((r,c))       #this will back track the shortest path
                        return

                


    #create rectangles or grid       

    def barloc(event):
        if can.find_withtag(CURRENT):
            can.itemconfig(CURRENT, fill="Black")
            X,Y=int((event.x)/box_g),int((event.y)/box_g)
            barries_points.append((Y,X))

    def desti(event):
        if can.find_withtag(CURRENT):
            can.itemconfig(CURRENT, fill="red")
            X,Y=int((event.x)/box_g),int((event.y)/box_g)
            detination_points.append((Y,X))

    def Barri():
        can.bind("<Button-1>",barloc)
        
    def chose_dest():
        can.bind("<Button-1>",desti)
        
    can = Canvas(root,width=canvas_w,height=canvas_h)
    can.grid(row=1,column=0)

    for row in range(int(canvas_w/box_g)):
        for col in range(int(canvas_h/box_g)):
            i = can.create_rectangle(row*box_g,col*box_g,row*box_g+box_g,col*box_g+box_g,fill="lightblue") 
            uid.append(i)

    mat_size.append((col,row))

    #Canvas for Action Buttons
    f = Canvas(root,width=canvas_w,height=50)
    f.grid(row=0,column=0)
    b1 = Button(f,text='choose Destination',fg = 'black',bg = 'green yellow',width=30,relief=SOLID,borderwidth=2,font = '30',padx=10,command=chose_dest)
    b1.grid(row=0,column=0,padx=50, pady=10)
    b2 = Button(f,text='Barriers',fg = 'black',bg = 'green yellow',width=30,relief=SOLID,borderwidth=2,font = '30',padx=10,command=Barri)
    b2.grid(row=0,column=1,padx=50, pady=10)
    b3 = Button(f,text='shortest',fg = 'black',bg = 'green yellow',width=30,relief=SOLID,borderwidth=2,font = '30',padx=10,command=search)
    b3.grid(row=0,column=3,padx=50, pady=10)
    mainloop()