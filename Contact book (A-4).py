
contacts = {}

def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number of the contact: ")
    contacts[name] = {"phone": phone}
    print(f"{name} has been added to your contacts.")

def search_contact():
    name = input("Enter the name of the contact you're looking for: ")
    if name in contacts:
        print(f"{name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print(f"{name} not found in your contacts.")

def display_contacts():
    if len(contacts) == 0:
        print("You have no contacts in your book.")
    else:
        print("Your contacts:")
        for name, info in contacts.items():
            print(f"{name}:")
            print(f"Phone: {info['phone']}")


while True:
    print("\nWelcome to your contact book!")
    print("What would you like to do?")
    print("1. Add a new contact")
    print("2. Search for a contact")
    print("3. Display all contacts")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
