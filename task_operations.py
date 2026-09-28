def add_task(tasks):
    task_name = input("Enter the new task: ")
    tasks.append({   "name": task_name })

    print("Task added successfully!")

def delete_task(tasks):
    try:
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print("Deleted:", removed["name"])
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")