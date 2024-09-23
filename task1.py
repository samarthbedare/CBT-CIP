# ContactMaster Application

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    
    if name in contacts:
        print(f"{name} already exists in contacts.")
    else:
        contacts[name] = number
        print(f"{name} added to your contacts.")


def delete_contact():
    name = input("Enter the name to delete the contact details of : ")
    
    if name in contacts:
        del contacts[name]
        print(f"{name} contact is deleted.")
    else:
        print(f"{name} does not exist.")


def search_contact():
    name = input("Enter the name you want to search: ")
    
    if name in contacts:
        print(f"Contact: {name}, Number: {contacts[name]}")
    else:
        print(f"{name} is not in your contacts.")


def display_contacts():
    if contacts:
        print("Your contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("Your contact list is empty.")


def main():
    while True:
        print("\nContactMasterApp")
        print("1. Add a new contact")
        print("2. Delete a contact")
        print("3. Search a contact")
        print("4. View all contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            delete_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            display_contacts()
        elif choice == '5':
            print("Exiting ContactMasterApp.")
            break
        else:
            print("Invalid input. Please select a valid option.")

if __name__ == "__main__":
    main()
