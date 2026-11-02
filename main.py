from datetime import datetime, date

tasks = []

def add_task():
    title = input("Enter task name: ").strip()

    while not title:
        title = input("Enter task name: ").strip()
    while True:
        Date = input("Enter due date (DD.MM.YYYY):")

        try:
            due_date = datetime.strptime(Date, "%d.%m.%Y").date()
            if due_date < date.today():
                print("Date cannot be in the past!")
                continue
            break
        except ValueError:
            print("Invalid date! Please use DD.MM.YYYY")


    note = input("Do you want to add notes?(y/n)").lower().strip()
    while(note != "n" and note != "y"):

        note = input("Do you want to add notes?(y/n)").lower().strip()
    if(note == "y"):
        Note = input("Enter your notes")
    else:
        Note = "No added Notes"


    task = {"title": title,"Date": Date,"completed": False, "Notes": Note}
    tasks.append(task)



def show_tasks():
    print("\033[1;34m===== Your Tasks =====\033[0m")

    if not tasks:
        print("No tasks available.")

    else:

        for task in tasks:
            print(task["title"])
            print(task["Date"])
            if(task["completed"] == False):
                print("Task is not completed")
            else:
                print("Task is completed")
            print(task["Notes"])
            print("____________")

def Complete_task():

    com = input("Write the completed Task:")

    found = False

    for task in tasks:
        if(com == task["title"]):
            task["completed"] = True
            found = True
            break
    if found:
        print("Task marked as completed!")
    else:
        print("Task not found!")

def delete_task():

    found = False
    deleted = input("Enter the task to delete:")

    for task in tasks:
        if(deleted == task["title"]):
            tasks.remove(task)
            found = True
            break

    if found:
        print("The task is deleted")
    else:
        print("The task is not found")

def menu():
        print("\033[1;34m===== Student Task Manager =====\033[0m")


        while True:

            print("1. Add task")
            print("2. Show Tasks")
            print("3. Delete Tasks")
            print("4. Complete Task")
            print("5. Exit")
            opt = input("Choose an option: ")

            if opt == "1":
                add_task()
            elif opt == "2":
                show_tasks()
            elif opt == "3":
                delete_task()
            elif opt == "4":
                Complete_task()
            elif opt == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option!")

menu()