import tkinter as tk
from tkinter import messagebox
from tkinter import *

canvas = tk.Tk()
canvas.title("Todo List")
canvas.geometry("800x1000")

window_height = 0
window_width = 0

def add_task():
    task = entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)

def get_window_dimensions():
    global window_height, window_width
    window_height = canvas.winfo_height()
    window_width = canvas.winfo_width()

    update_listbox_size()

def update_listbox_size():
    tasks_listbox_width = window_width - 100
    tasks_listbox_height = window_height - 100
    print(tasks_listbox_height, tasks_listbox_width)

    tasks_listbox.config(width=tasks_listbox_width, height=tasks_listbox_height)


Image_icon = PhotoImage(file='ToDoListPy/Assets/task.png')
canvas.iconphoto(False, Image_icon)

TopImage = PhotoImage(file="ToDoListPy/Assets/topbar.png")
Label(canvas, image = TopImage).pack()

entry = tk.Entry(canvas)
entry.pack()

add_button = tk.Button(canvas, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(canvas, text="Delete Task", command=delete_task)
delete_button.pack()

tasks_listbox = tk.Listbox(canvas)
tasks_listbox.pack()
canvas.after(200, get_window_dimensions)

canvas.mainloop()
