# Example: Simple contact manager
contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Added {name}")

def show_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def start():
    while True:
        action = input("Add (a) or Show (s) or Quit (q): ")
        if action == "q":
            break
        elif action == "a":
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(name, phone)
        elif action == "s":
            show_contacts()