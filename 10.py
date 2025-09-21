from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)
w.grid(row =0 , column= 1)
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.grid(row =50 , column= 50)
top = Toplevel()
mainloop()