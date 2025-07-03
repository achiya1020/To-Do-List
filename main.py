import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x500")
root.title("TO-DO LIST")

title_label = tk.Label(root, text="TO-DO LIST", font=("Arial", 25, "bold"))
title_label.pack(pady=10)

list_frame = tk.Frame(root)
list_frame.pack()

lb = tk.Listbox(
    list_frame,
    width=55,
    height=10,
    font="Arial",
    bd=0,
    highlightthickness=1,
    selectbackground="lightblue",
    activestyle="none"
)
lb.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
lb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)


entry_frame = tk.Frame(root)
entry_frame.pack(pady=20)

my_entry = tk.Entry(entry_frame, font=("Arial", 14), width=30, borderwidth=2)
my_entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(entry_frame, text="Add Task", command=lambda: newTask(), width=10)
add_btn.pack(side=tk.LEFT)

bottom_btns_frame = tk.Frame(root)
bottom_btns_frame.pack(fill="x", pady=20, padx=20)

mark_btn = tk.Button(bottom_btns_frame, text="✓ Mark as Read", command=lambda: markAsRead(), width=15)
mark_btn.pack(side=tk.LEFT)

delete_btn = tk.Button(bottom_btns_frame, text=" Delete Task", command=lambda: deleteTask(), width=15)
delete_btn.pack(side=tk.RIGHT)


def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(tk.END, task)
        my_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter some task")

def deleteTask():
    lb.delete(tk.ANCHOR)

def markAsRead():
    selected = lb.curselection()
    if selected:
        current_text = lb.get(selected)
        if not current_text.startswith("✓ "):
            lb.delete(selected)
            lb.insert(selected, "✓ " + current_text)
    else:
        messagebox.showinfo("Info", "Please select a task to mark as read")

root.mainloop()
