
from datetime import datetime, date
import shutil

tasks = []

# Colors
RESET = "\033[0m"
BOLD = "\033[1m"

BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
PURPLE = "\033[1;35m"
WHITE = "\033[1;37m"


# Center text in terminal
def center(text):
    width = shutil.get_terminal_size(fallback=(100, 24)).columns
    spaces = max(0, (width - len(text)) // 2)
    return " " * spaces + text

def print_center(text, color=RESET):
    width = shutil.get_terminal_size(fallback=(100, 24)).columns
    spaces = max(0, (width - len(text)) // 2)
    print(" " * spaces + color + text + RESET)


def input_center(text, color=YELLOW):
    return input(center(color + text + RESET))


def print_line():
    width = min(60, shutil.get_terminal_size(fallback=(100, 24)).columns - 4)
    print_center("═" * max(10, width), BLUE)


# Add task
def add_task():

    print()
    print_center("╔══════════════════════════════════════╗", BLUE)
    print_center("           ADD NEW TASK", BLUE + BOLD)
    print_center("╚══════════════════════════════════════╝", BLUE)

    title = input_center("Enter task name: ").strip()

    while not title:
        print_center("Task name cannot be empty!", RED)
        title = input_center("Enter task name: ").strip()

    while True:
        Date = input_center("Enter due date (DD.MM.YYYY): ").strip()

        try:
            due_date = datetime.strptime(Date, "%d.%m.%Y").date()

            if due_date < date.today():
                print_center("Date cannot be in the past!", RED)
                continue

            break

        except ValueError:
            print_center("Invalid date! Please use DD.MM.YYYY", RED)

    note = input_center("Do you want to add notes? (y/n): ").lower().strip()

    while note != "n" and note != "y":
        print_center("Please enter y or n!", RED)
        note = input_center("Do you want to add notes? (y/n): ").lower().strip()

    if note == "y":
        Note = input_center("Enter your notes: ").strip()
    else:
        Note = "No added Notes"

    for task in tasks:
        if task["title"].lower() == title.lower() and task["Date"] == Date:
            print_center("Task already exists!", RED)
            return

    task = {
        "title": title,
        "Date": Date,
        "completed": False,
        "Notes": Note
    }

    tasks.append(task)

    print()
    print_center("✔ Task added successfully!", GREEN + BOLD)
    print()


# Show tasks
def show_tasks():

    print()
    print_center("╔══════════════════════════════════════╗", BLUE)
    print_center("             YOUR TASKS", BLUE + BOLD)
    print_center("╚══════════════════════════════════════╝", BLUE)

    if not tasks:
        print_center("No tasks available.", YELLOW)

    else:
        for i, task in enumerate(tasks, start=1):

            print()
            print_center(f"┌──────────── TASK {i} ────────────┐", PURPLE + BOLD)
            print_center(f"Title: {task['title']}", CYAN)
            print_center(f"Due date: {task['Date']}", WHITE)

            if task["completed"]:
                print_center("✔ Completed", GREEN)
            else:
                print_center("○ Not completed", YELLOW)

            print_center(f"Notes: {task['Notes']}", WHITE)
            print_center("└─────────────────────────────────┘", PURPLE)

    print()


# Complete task
def Complete_task():

    if not tasks:
        print_center("No tasks available.", YELLOW)

    else:
        print()
        com = input_center("Write the completed task: ").strip()
        while True:
            com_date = input_center("Enter the date (DD.MM.YYYY): ").strip()

            try:
                due_date = datetime.strptime(com_date, "%d.%m.%Y").date()
                break

            except ValueError:
                print_center("Invalid date! Please use DD.MM.YYYY", RED)


        found = False

        for task in tasks:
            if com.lower() == task["title"].lower() and due_date == datetime.strptime(task["Date"], "%d.%m.%Y").date():
                task["completed"] = True
                found = True
                break

        if found:
            print_center("✔ Task marked as completed!", GREEN)
        else:
            print_center("Task not found!", RED)


# Delete task
def delete_task():

    if not tasks:
        print_center("No tasks available.", YELLOW)

    else:
        found = False

        print()
        deleted = input_center("Enter the task to delete: ").strip()

        while True:
            com_date = input_center("Enter the date (DD.MM.YYYY): ").strip()

            try:
                due_date = datetime.strptime(com_date, "%d.%m.%Y").date()
                break

            except ValueError:
                print_center("Invalid date! Please use DD.MM.YYYY", RED)

        for task in tasks:
            if deleted.lower() == task["title"].lower() and due_date == datetime.strptime(task["Date"], "%d.%m.%Y").date():
                tasks.remove(task)
                found = True
                break

        if found:
            print_center("✔ The task is deleted!", GREEN)
        else:
            print_center("The task was not found!", RED)


# Main menu
def menu():

    while True:

        print("\n")
        print_center("╔════════════════════════════════════════════╗", BLUE)
        print_center("║                                            ║", BLUE)
        print_center("║          STUDENT TASK MANAGER              ║", BLUE + BOLD)
        print_center("║                                            ║", BLUE)
        print_center("╚════════════════════════════════════════════╝", BLUE)

        print()
        print_center("       [1]  Add Task", CYAN)
        print_center("       [2]  Show Tasks", CYAN)
        print_center("       [3]  Delete Task", CYAN)
        print_center("       [4]  Complete Task", CYAN)
        print_center("       [5]  Exit", CYAN)

        print()
        print_line()

        opt = input_center("Choose an option: ").strip()

        if opt == "1":
            add_task()

        elif opt == "2":
            show_tasks()

        elif opt == "3":
            delete_task()

        elif opt == "4":
            Complete_task()

        elif opt == "5":
            print()
            print_center("Thank you for using Student Task Manager!", GREEN + BOLD)
            print_center("Have a productive day! Goodbye!", GREEN)
            print()
            break

        else:
            print_center("Invalid option! Please try again.", RED)


menu()
