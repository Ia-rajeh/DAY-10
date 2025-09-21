import tkinter as tk

root = tk.Tk()
root.title("DAY 10")

# Create three buttons
button1 = tk.Button(root, text="NAME 1")
button2 = tk.Button(root, text="NAME 2")
button3 = tk.Button(root, text="NAME 3")

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()

root.mainloop()