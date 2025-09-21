from tkinter import *
main = Tk()
ourMessage = 'DAY 10'
messageVar = Message(main, text=ourMessage , fg = "blue" , bg = "red")

messageVar.grid( row = 1000 , column = 100)
main.mainloop()