"""
Contact Book — Complete Solution

A CLI contact book application using dict for in-memory storage.
"""

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        overwrite = input(f"'{name}' already exists. Overwrite? (y/n): ").lower()
        if overwrite != "y":
            print("Cancelled.")
            return

    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {"name": name, "phone": phone, "email": email}
    print(f"Contact '{name}' added successfully.")


def view_all():
    if not contacts:
        print("No contacts found.")
        return

    print(f"\n{'Name':<20} {'Phone':<15} {'Email':<25}")
    print("-" * 60)
    for contact in contacts.values():
        print(f"{contact['name']:<20} {contact['phone']:<15} {contact['email']:<25}")
    print()


def search_contact():
    name = input("Enter name to search: ").strip()
    contact = contacts.get(name)
    if contact:
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"Contact '{name}' not found.")


def update_contact():
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print(f"Contact '{name}' not found.")
        return

    print("Leave blank to keep current value.")
    phone = input(f"Phone ({contacts[name]['phone']}): ").strip()
    email = input(f"Email ({contacts[name]['email']}): ").strip()

    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    print(f"Contact '{name}' updated.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Delete '{name}'? (y/n): ").lower()
        if confirm == "y":
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Cancelled.")
    else:
        print(f"Contact '{name}' not found.")


def main():
    while True:
        print("\n=== Contact Book ===")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        print("=" * 20)

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1-6.")


if __name__ == "__main__":
    main()
