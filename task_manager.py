# Required Modules
import json

# Creating a empty tasks list
tasks = []

#  open the tasks file
try:
    x = open("tasks.json", 'x')
    x.close()
except FileExistsError:
    pass


# Function to save tasks to the  file
def save_tasks():
    with open("tasks.json", 'w') as file:
        for task in tasks:
            file.write(f"Title: {task['title']}\n")
            file.write(f"Description: {task['description']}\n")
            file.write(f"Status: {'True' if task['completed'] else 'False'}\n\n")


# Function to load tasks from the  file
def load_tasks():
    try:
        with open("tasks.json", 'r') as file:
            lines = file.readlines()
            task_info = {"title": "", "description": "", "completed": False}
            for line in lines:
                line = line.strip()
                if line.startswith("Title: "):
                    task_info["title"] = line[len("Title: "):]
                elif line.startswith("Description: "):
                    task_info["description"] = line[len("Description: "):]
                elif line.startswith("Status: "):
                    task_info["completed"] = (line[len("Status: "):] == "completed")
                elif not line:
                    tasks.append(task_info)
                    task_info = {"title": "", "description": "", "completed": False}
    except FileNotFoundError:
        return []


# view_tasks function
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. Title: {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Status: {'True' if task['completed'] else 'False'}")


#  adding new task to the list of tasks 
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")

    task = {
        "title": title,
        "description": description,
        "completed": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


# updating the status of the task as Ture
def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the index of the task that you want to mark as completed: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            save_tasks()
            print("Task Marked as Completed ✅")
        else:
            print("Enter a valid task index.")
    except ValueError:
        print("Invalid Input. Please enter a valid number")

# deteting a task from the file
def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            save_tasks()  # Save the updated tasks list back to the file
            print(f"Task '{deleted_task['title']}' deleted successfully!")
        else:
            print("Invalid task index.")
   

# main function
def main():
    load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. delete task")
        print("5. Quit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                view_tasks()
            elif choice == 2:
                add_task()
            elif choice == 3:
                mark_completed()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting the Task Manager. Thank you!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# run program
if __name__ == "__main__":
    main()