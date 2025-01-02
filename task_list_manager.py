import os

def add_task():
    task = input("Enter the task: ")
    try:
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print("Task added successfully.")
    except IOError:
        print("An error occurred while writing to the file.")

def remove_task():
    task_to_remove = input("Enter the task to remove: ")
    try:
        if not os.path.exists("tasks.txt"):
            raise FileNotFoundError("No tasks found.")
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        with open("tasks.txt", "w") as file:
            for task in tasks:
                if task.strip() != task_to_remove:
                    file.write(task)
        print("Task removed successfully.")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError:
        print("An error occurred while reading or writing to the file.")

def view_tasks():
    try:
        if not os.path.exists("tasks.txt"):
            raise FileNotFoundError("No tasks found.")
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("Your tasks:")
                for task in tasks:
                    print(f"- {task.strip()}")
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except IOError:
        print("An error occurred while reading the file.")

def main():
    while True:
        print("\nTask List Manager")
        print("1. Add a new task")
        print("2. Remove a task")
        print("3. View all tasks")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
