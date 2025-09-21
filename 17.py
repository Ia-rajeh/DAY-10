from tkinter import *
master = Tk()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y )
w.create_arc(1, 2 ,3 ,start = 0 , extent = 190 , fill = "red")
mainloop()