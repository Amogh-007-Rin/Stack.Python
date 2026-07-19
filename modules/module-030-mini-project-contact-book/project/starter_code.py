"""
Contact Book — Starter Code

Fill in the function bodies to complete the contact book application.
"""

contacts = {}


def add_contact():
    """Prompt for name, phone, email and add to contacts dict."""
    # TODO: Get name input
    # TODO: Check if name already exists — ask to overwrite
    # TODO: Get phone and email
    # TODO: Store as contacts[name] = {"name": name, "phone": phone, "email": email}
    pass


def view_all():
    """Display all contacts in a formatted table."""
    # TODO: Handle empty contacts
    # TODO: Print header and each contact
    pass


def search_contact():
    """Look up a contact by name and display details."""
    # TODO: Get name input
    # TODO: Use contacts.get(name) to find contact
    # TODO: Display details or "not found" message
    pass


def update_contact():
    """Update phone and/or email for an existing contact."""
    # TODO: Get name input
    # TODO: Check if contact exists
    # TODO: Show current values, allow blank to keep
    pass


def delete_contact():
    """Remove a contact by name."""
    # TODO: Get name input
    # TODO: Check if exists, ask confirmation, delete
    pass


def main():
    """Main menu loop."""
    while True:
        print("\n=== Contact Book ===")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")
        print("=" * 20)

        # TODO: Get user choice and call the appropriate function


if __name__ == "__main__":
    main()
