import datetime
import calendar

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as x:
            for line in x:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    tasks.append({
                        "task": parts[0],
                        "priority": parts[1],
                        "duedate": parts[2],
                        "note": parts[3],
                        "status": parts[4]
                    })
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as x:
        for t in tasks:
            line = f"{t['task']}|{t['priority']}|{t['duedate']}|{t['note']}|{t['status']}\n"
            x.write(line)


def priority_emoji(priority):
    if priority == "High":
        return "🔴"
    elif priority == "Medium":
        return "🟡"
    else:
        return "🟢"


def add_task(tasks):
    task_name = input("Enter the task: ")
    
    print("Select priority: 1. High  2. Medium  3. Low")
    choice = input("Enter choice (1/2/3): ")
    if choice == "1":
        priority = "High"
    elif choice == "2":
        priority = "Medium"
    else:
        priority = "Low"
    
    duedate = input("Enter due date (DD-MM-YYYY): ")
    note = input("Enter a short note (optional): ")[:50]
    
    tasks.append({
        "task": task_name,
        "priority": priority,
        "duedate": duedate,
        "note": note,
        "status": "Pending"
    })
    save_tasks(tasks)
    print("Task added successfully!\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
        return
    
    print("\n--- Your Tasks ---")
    for i, t in enumerate(tasks, start=1):
        emoji = priority_emoji(t["priority"])
        print(f"{i}. {emoji} {t['task']} | Due: {t['duedate']} | Note: {t['note']} | Status: {t['status']}")
    print()


def view_calendar():
    now = datetime.datetime.now()
    print(calendar.month(now.year, now.month))


def show_clock():
    now = datetime.datetime.now()
    print("Current date & time:", now.strftime("%d-%m-%Y %H:%M:%S"), "\n")


def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    choice = input("Enter the task number to mark as complete: ")
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        tasks[int(choice) - 1]["status"] = "Completed"
        save_tasks(tasks)
        print("Task marked as complete!\n")
    else:
        print("Invalid choice.\n")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    choice = input("Enter the task number to delete: ")
    if choice.isdigit() and 1 <= int(choice) <= len(tasks):
        removed = tasks.pop(int(choice) - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['task']}\n")
    else:
        print("Invalid choice.\n")


def main():
    tasks = load_tasks()
    
    while True:
        print("=== To-Do List ===")
        print("1. Add a new task")
        print("2. View existing tasks")
        print("3. View this month's calendar")
        print("4. Show current date & time")
        print("5. Mark a task as complete")
        print("6. Delete a task")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_calendar()
        elif choice == "4":
            show_clock()
        elif choice == "5":
            mark_complete(tasks)
        elif choice == "6":
            delete_task(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")


main()