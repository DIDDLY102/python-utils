# todo.py
TODO_FILE = "tasks.txt"

def add_task(task):
    with open(TODO_FILE, "a") as f:
        f.write(task + "\n")
    print(f"Task added: {task}")

def view_tasks():
    try:
        with open(TODO_FILE, "r") as f:
            tasks = f.readlines()
        if not tasks:
            print("No tasks yet!")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks file found!")

if __name__ == "__main__":
    print("Todo List Manager")
    print("1. Add Task")
    print("2. View Tasks")
    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
      
