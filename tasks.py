def loadTasks():
    try:
        with open("todo.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def saveTasks(tasks):
    with open("todo.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def addTask():
    tasks = loadTasks()
    task = input("Enter a task: ")
    tasks.append(task)
    saveTasks(tasks)
    print(f"Task '({task} +1)' added successfully!")
    print("------------------------------------")


def listTasks():
    tasks = loadTasks()
    if not tasks:
        print("No tasks found.")
        print("------------------------------------")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print("------------------------------------")


def deleteTask():
    tasks = loadTasks()
    listTasks()
    try:
        task2Delete = int(input("Enter the number of the task to delete: "))
        if 1 <= task2Delete <= len(tasks):
            deletedTask = tasks.pop(task2Delete - 1)
            saveTasks(tasks)
            print(f"Task '{deletedTask}' deleted successfully!")
            print("------------------------------------")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please try again.")
        print("------------------------------------")


if __name__ == "__main__":
    ### Create a loop to run the app
    print("To-Do List Application v0.1")
    while True:
        print("\n")
        print("Select one of the following options:")
        print("------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. View all tasks")
        print("4. Exit the application")

        choice = input("Choice: ")
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again, selecting an option from 1 to 4.")

    print("Farewell, friend! 👋")
