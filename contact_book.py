# contact_book.py
import json
import os
import sys

DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "contacts.json")

def ensure_storage():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

def load_contacts():
    ensure_storage()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=2)

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()

    if not name or not phone:
        print("Name and phone are required!")
        return

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully.")

def list_contacts():
    print("\n--- Contact List ---")
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']} | {c.get('email', '')} | {c.get('address', '')}")

def search_contact():
    print("\n--- Search Contact ---")
    key = input("Enter name or phone to search: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if key in c["name"].lower() or key in c["phone"]]
    if not results:
        print("No contact found.")
        return
    for i, c in enumerate(results, 1):
        print(f"{i}. {c['name']} - {c['phone']} | {c.get('email', '')} | {c.get('address', '')}")

def update_contact():
    print("\n--- Update Contact ---")
    list_contacts()
    try:
        index = int(input("Enter contact number to update: ")) - 1
        contacts = load_contacts()
        if index < 0 or index >= len(contacts):
            print("Invalid selection.")
            return
        c = contacts[index]
        print("Leave blank to keep existing value.")
        name = input(f"Name [{c['name']}]: ").strip() or c['name']
        phone = input(f"Phone [{c['phone']}]: ").strip() or c['phone']
        email = input(f"Email [{c.get('email','')}]: ").strip() or c.get('email','')
        address = input(f"Address [{c.get('address','')}]: ").strip() or c.get('address','')
        contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
        save_contacts(contacts)
        print(f"✅ Contact '{name}' updated successfully.")
    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    print("\n--- Delete Contact ---")
    list_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        contacts = load_contacts()
        if index < 0 or index >= len(contacts):
            print("Invalid selection.")
            return
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"🗑️ Contact '{removed['name']}' deleted successfully.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while True:
        print("\n📒 === CONTACT BOOK MENU ===")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            list_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book. Bye!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose between 1-6.")

if __name__ == "__main__":
    menu()
