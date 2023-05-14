import tkinter as tk

class ToDoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.tasks = []
        self.task_list = tk.Listbox(self.master, height=10, width=50)
        self.task_list.pack()
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.pack()
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        self.remove_task_button = tk.Button(self.master, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
            
    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = int(selected_task[0])
            self.task_list.delete(index)
            del self.tasks[index]

root = tk.Tk()
app = ToDoList(root)
root.mainloop()
