import file_manager
import task_operations
import menu_display

def main():
    tasks = file_manager.load_tasks()
    while True:
        menu_display.show_menu()
        choice = input("\nEnter your choice: ")

        if choice== "1":
            task_operations.add_task(tasks)
            file_manager.save_tasks(tasks)
        elif choice =="2":
            menu_display.show_tasks(tasks)
            input("\nPress Enter to continue...")
        elif choice=="3":
            task_operations.delete_task(tasks)
            file_manager.save_tasks(tasks)
        elif choice =="4":
            print("have a nice day!")
            break
        else:
            print("Invalid choice!")

if __name__ =="__main__":
    main()
