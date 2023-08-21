import tkinter
import tkinter.messagebox
import pickle
root=tkinter.Tk()
root.title("Todo List")
def add_task():
    todo=task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention",message="To add a task please enter some task")
def task_remove():
    try:
        index_todo = todo_box.curselection()[0]  # Use todo_box instead of list_frame
        todo_box.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="Attention", message="To delete a task you must select the task")

def task_load():
    try:
        todo_list = pickle.load(open("task.dat", "rb"))
        todo_box.delete(0, tkinter.END)  # Clear the existing list box
        for todo in todo_list:
            todo_box.insert(tkinter.END, todo)
    except FileNotFoundError:  # Use a specific exception
        tkinter.messagebox.showwarning(title="Attention", message="Can't find task.dat")

def task_save():
    todo_list = todo_box.get(0, tkinter.END)  # Get tasks from the Listbox
    pickle.dump(todo_list, open("task.dat", "wb"))
list_frame=tkinter.Frame(root)
list_frame.pack()
todo_box=tkinter.Listbox(list_frame,height=20,width=50)
todo_box.pack(side=tkinter.LEFT)
scroller=tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill=tkinter.Y)
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)
task_add=tkinter.Entry(root,width=70)
task_add.pack()
addtaskbutton = tkinter.Button(root, text="Click to add task", font=('arial', 20, 'bold'), background='red', width=40, command=add_task)  # Change "task_add" to "add_task"

addtaskbutton.pack()
removetaskbutton=tkinter.Button(root,text="Click to remove task",font=('arail',20,'bold'),background='yellow',width=40,command=task_remove)
removetaskbutton.pack()
loadtaskbutton=tkinter.Button(root,text="Click to load task",font=('arail',20,'bold'),background='green',width=40,command=task_load)
loadtaskbutton.pack()
savetaskbutton=tkinter.Button(root,text="Click to save task",font=('arail',20,'bold'),background='blue',width=40,command=task_save)
savetaskbutton.pack()

root.mainloop()