# todo_list.py
import json, os, sys

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "todos.json")

def ensure_storage():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_todos():
    ensure_storage()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, indent=2)

def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks yet.")
        return
    print("\nYour To-Do List:")
    for i, t in enumerate(todos, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['text']}")
    print()

def add_todo():
    text = input("Task: ").strip()
    if not text:
        print("Empty task ignored.")
        return
    todos = load_todos()
    todos.append({"text": text, "done": False})
    save_todos(todos)
    print("Added.")

def update_todo():
    list_todos()
    try:
        idx = int(input("Which task number to update? ")) - 1
        todos = load_todos()
        if idx < 0 or idx >= len(todos):
            print("Invalid index.")
            return
        new_text = input("New text: ").strip()
        if new_text:
            todos[idx]["text"] = new_text
            save_todos(todos)
            print("Updated.")
    except ValueError:
        print("Please enter a number.")

def complete_todo():
    list_todos()
    try:
        idx = int(input("Which task number to mark complete? ")) - 1
        todos = load_todos()
        if idx < 0 or idx >= len(todos):
            print("Invalid index.")
            return
        todos[idx]["done"] = True
        save_todos(todos)
        print("Completed.")
    except ValueError:
        print("Please enter a number.")

def delete_todo():
    list_todos()
    try:
        idx = int(input("Which task number to delete? ")) - 1
        todos = load_todos()
        if idx < 0 or idx >= len(todos):
            print("Invalid index.")
            return
        removed = todos.pop(idx)
        save_todos(todos)
        print(f"Deleted: {removed['text']}")
    except ValueError:
        print("Please enter a number.")

def menu():
    actions = {
        "1": ("List tasks", list_todos),
        "2": ("Add task", add_todo),
        "3": ("Update task", update_todo),
        "4": ("Complete task", complete_todo),
        "5": ("Delete task", delete_todo),
        "6": ("Exit", None),
    }
    while True:
        print("\n=== TO-DO LIST ===")
        for k, (label, _) in actions.items():
            print(f"{k}. {label}")
        choice = input("Choose: ").strip()
        if choice == "6":
            print("Bye!")
            sys.exit(0)
        action = actions.get(choice)
        if action:
            action[1]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
