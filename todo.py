tasks = []


# function to add task
def add_task():
    task_name = input("Enter task: ")
    task = {"task": task_name, "done": False}
    tasks.append(task)
    print("Task added successfully!\n")


# function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available\n")
        return

    print("\nYour Tasks:")
    for i, task in enumerate(tasks):
        status = "✓" if task["done"] else "✗"
        print(f"{i+1}. {task['task']} [{status}]")
    print()


# function to mark task completed
def complete_task():
    view_tasks()

    if not tasks:
        return

    num = int(input("Enter task number to mark complete: "))

    if 1 <= num <= len(tasks):
        tasks[num-1]["done"] = True
        print("Task marked as completed!\n")
    else:
        print("Invalid task number\n")

# function to delete task
def delete_task():
    view_tasks()

    if not tasks:
        return

    num = int(input("Enter task number to delete: "))
    tasks.pop(num-1)
    print("Task deleted!\n")


# main program loop
while True:

    print("==== TO DO LIST ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice\n")