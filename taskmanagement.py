import datetime

tasks = []

def add_task():
    task_name = input("Enter task name: ")
    task_time = input("Enter task time (hh:mm): ")
    try:
        task_time = datetime.datetime.strptime(task_time, '%H:%M')
        tasks.append((task_name, task_time))
        print("Task added successfully!")
    except ValueError:
        print("Invalid time format. Please use hh:mm format.")

def list_tasks():
    for idx, (task_name, task_time) in enumerate(tasks):
        print(f"{idx + 1}. {task_name} - {task_time.strftime('%H:%M')}")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()