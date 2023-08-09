import tkinter as tk

def button_click():
    label.config(text="Created new ToDo")

canvas = tk.Tk()
canvas.title("ToDo Liste")
canvas.minsize(800,800)
canvas.maxsize(1400, 1000)

label = tk.Label(canvas, text="Hello")
label.pack()

button = tk.Button(canvas, text="New Todo", command=button_click)
button.pack()


canvas.mainloop()

