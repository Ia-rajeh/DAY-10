import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

root = tk.Tk()
root.title("day 10")

# Create a label
label = tk.Label(root, text="Selected Item: ")
label.pack(pady=10)

# Create a Combobox widget
combo_box = ttk.Combobox(root, values=["ahmed", "ana", "khaled"], state='readonly')
combo_box.pack(pady=5)

# Set default value
combo_box.set("names")

# Bind event to selection
combo_box.bind("<<ComboboxSelected>>", select)
root.mainloop()