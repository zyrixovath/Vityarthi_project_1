def show_tasks(tasks):
    print("=" * 40)
    print("          MY TO-DO LIST")
    print("=" * 40)

    if len(tasks) == 0:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(i + 1, task["name"])
    print("=" * 40)

def show_menu():
    print("\n1. Add a task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")