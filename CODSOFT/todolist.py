import tkinter as tk
from tkinter import messagebox
import json, os
from datetime import datetime

DATA_FILE = "my_tasks.json"

def read_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def write_data():
    with open(DATA_FILE, "w") as f:
        json.dump(todo_items, f, indent=2)

def refresh_view():
    task_box.delete(0, tk.END)
    for item in todo_items:
        state = "✔ Done" if item["finished"] else "❌ Pending"
        deadline = item["deadline"] if item["deadline"] else "No date"
        task_box.insert(tk.END, f"{item['title']}  |  {deadline}  |  {state}")

def add_item():
    title = task_input.get().strip()
    date = date_input.get().strip()
    if not title:
        messagebox.showerror("Error", "Task cannot be empty!")
        return
    if date:
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date must be YYYY-MM-DD or blank.")
            return
    todo_items.append({"title": title, "finished": False, "deadline": date})
    write_data()
    refresh_view()
    task_input.delete(0, tk.END)
    date_input.delete(0, tk.END)

def mark_done():
    try:
        idx = task_box.curselection()[0]
        todo_items[idx]["finished"] = True
        write_data()
        refresh_view()
    except IndexError:
        messagebox.showwarning("Select Task", "Pick a task first!")

def remove_item():
    try:
        idx = task_box.curselection()[0]
        del todo_items[idx]
        write_data()
        refresh_view()
    except IndexError:
        messagebox.showwarning("Select Task", "Pick a task first!")

app = tk.Tk()
app.title("My To-Do List")
app.geometry("600x400")

todo_items = read_data()

frame = tk.Frame(app)
frame.pack(pady=10)

task_box = tk.Listbox(frame, width=70, height=12, bg="#f9f9f9", fg="#333")
task_box.pack(side=tk.LEFT)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
task_box.config(yscrollcommand=scroll.set)
scroll.config(command=task_box.yview)

task_input = tk.Entry(app, width=40)
task_input.pack(pady=5)
task_input.insert(0, "Enter new task")

date_input = tk.Entry(app, width=20)
date_input.pack(pady=5)
date_input.insert(0, "YYYY-MM-DD (optional)")

btn_frame = tk.Frame(app)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="➕ Add Task", width=15, command=add_item).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="✔ Mark Done", width=15, command=mark_done).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="🗑 Delete Task", width=15, command=remove_item).grid(row=0, column=2, padx=5)

refresh_view()
app.mainloop()
