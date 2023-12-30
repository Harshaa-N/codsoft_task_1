import tkinter as tk
from tkinter import *
from tkinter import messagebox

root = tk.Tk()
root.title("My To-Do List")
root.iconbitmap("todo-list.ico")
root.geometry("600x600")
root.config(bg="maroon1")

def add_task():
    task = entry.get()
    if task:
        if task not in tasks:
            tasks.append(task)
            listbox.insert(tk.END, task)
        else:
            tk.messagebox.showinfo(title="Error", message="Task is already exists")
    entry.delete(0, tk.END)  
def update_task():
    selected_task = listbox.get(tk.ANCHOR)
    if selected_task:
        new_task = entry.get()
        if new_task:
            index = listbox.curselection()[0]
            tasks[index] = new_task
            listbox.delete(index)
            listbox.insert(index, new_task)
        else:
            tk.messagebox.showinfo(title="Error", message="Please enter a new task")
    entry.delete(0, tk.END)
def delete_task():
    selected_task = listbox.get(tk.ANCHOR)
    if selected_task:
        index = listbox.curselection()[0]
        del tasks[index]
        listbox.delete(index)
def mark_task_done():
    selected_task = listbox.get(tk.ANCHOR)
    if selected_task:
        index = listbox.curselection()[0]
        tasks[index] = f"~{tasks[index]}"  
        listbox.delete(index)
        listbox.insert(index, tasks[index])
def mark_task_undone():
    selected_task = listbox.get(tk.ANCHOR)
    if selected_task and selected_task.startswith("~"):
        index = listbox.curselection()[0]
        tasks[index] = tasks[index][1:]  
        listbox.delete(index)
        listbox.insert(index, tasks[index])
        
tasks = []

label=Label(root, text="To-Do List:",font=("Arialblack",15))
label.pack()

entry =tk.Entry(root,width=50,font=("Arialblack",15))
entry.pack(ipady=20)

add_btn=Button(root, text="TASK ADDED", command=add_task,width=10,padx=30,pady=10,bg="lightgreen")
add_btn.pack()

delete_btn =Button(root, text="TASK DELETED", command=delete_task,width=10,padx=30,pady=10,bg="red")
delete_btn.pack()

update_btn=Button(root, text="TASK UPDATED", command=update_task,width=10,padx=30,pady=10,bg="skyblue")               
update_btn.pack()

mark_btn=Button(root, text="TASK MARKED", command=mark_task_done,width=10,padx=30,pady=10,bg="lightsalmon1")
mark_btn.pack()

unmark_btn=Button(root, text="TASK UNMARKED", command=mark_task_undone,width=10,padx=30,pady=10,bg="burlywood1")
unmark_btn.pack()

listbox =Listbox(root,width=35,height=30,font=("Arialblack",15))
listbox.pack(pady=10)

root.mainloop()
