from src.cli import populate_menu
from src.storage import ensure_file_exists
from src.tracker import taskTracker
def main():
    menu = populate_menu()

    tracker = taskTracker()

    while True:
        print(menu)

        user_input = int(input(">> "))

        match user_input:
            case 1: #add task
                description = input("Enter task description: ")
                tracker.add(description)
            case 2: #update task
                task_id = input("Enter task ID to update: ")
                new_description = input("Enter new task description: ")
                
                tracker.update(task_id, new_description)
            case 3: #delete task
                task_id = input("Enter task ID to delete: ")
                tracker.delete(task_id)
            case 4: #toggle task status
                task_id = input("enter task ID to toggle status: ")
                new_status = tracker.toggle_status(task_id)
                print(f"new status : {new_status.capitalize()}\n")
            case 8: #exit
                print("task tracker exiting...Goodbye!")
                break  
if __name__ == "__main__":
    ensure_file_exists()
    main()