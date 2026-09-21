tasks = [] 

def menu():
    print("\n" + "-"*25)
    print("     MY TO-DO LIST")
    print("-"*25)
    print("1. View my tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Quit")
    print("-"*25)

while True:
    menu()
    choice = input("Choose an option (1/2/3/4): ")

    if choice=='1' or choice.lower()=="view my tasks":
        print("\n--- Your Tasks ---")
        if len(tasks) == 0:
            print("Your list is empty! Relax.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
                
    elif choice == '2' or choice.lower()=="add a task":
        new_task = input("\nEnter the new task: ")
        tasks.append(new_task)
        print(f"'{new_task}' added to your list!")

    elif choice == '3' or choice.lower()=="delete a task":
        if len(tasks) == 0:
            print("\nThere are no tasks to delete!")
        else:
            print("\n--- Your Tasks ---")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            
            task_num = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"'{removed_task}' has been deleted!")
            else:
                print("Invalid task number.")

    elif choice == '4' or choice.lower()=="quit":
        print("\nGoodbye! Have a productive day.")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, 3, or 4.")
