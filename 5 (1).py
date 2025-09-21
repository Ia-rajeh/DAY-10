from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='YES', variable=v, value=1).grid(row=0, column=1)
Radiobutton(root, text='NO', variable=v, value=2).grid(row=5, column=1)
mainloop()