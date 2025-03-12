import requests

API_URL = "http://127.0.0.1:8000/tasks/"

def display_tasks():
    response = requests.get(API_URL)
    tasks = response.json()
    for task in tasks:
        print(f"{task['id']}. [{ '✔' if task['completed'] else ' ' }] {task['title']} - Priority: {task['priority']}")

def create_task():
    title = input("Task Title: ")
    description = input("Task Description: ")
    priority = int(input("Priority (1-5): "))
    deadline = input("Deadline (YYYY-MM-DD): ")

    response = requests.post(API_URL, json={
        "title": title,
        "description": description,
        "priority": priority,
        "deadline": deadline
    })
    print(response.json()["message"])

def delete_task():
    task_id = input("Enter Task ID to Delete: ")
    response = requests.delete(f"{API_URL}{task_id}")
    print(response.json()["message"])

def main():
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Delete Task\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            create_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
