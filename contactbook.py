import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts.append(Contact(name, phone, email, address))
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name}: {contact.phone}")

    def search_contact(self):
        query = input("Enter name or phone number to search: ")
        results = [c for c in self.contacts if query.lower() in c.name.lower() or query in c.phone]
        if results:
            for i, contact in enumerate(results, 1):
                print(f"{i}. {contact.name}: {contact.phone}")
        else:
            print("No matching contacts found.")

    def update_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to update: ")) - 1
            contact = self.contacts[index]
            print(f"Updating {contact.name}")
            contact.name = input("Enter new name (or press enter to keep current): ") or contact.name
            contact.phone = input("Enter new phone (or press enter to keep current): ") or contact.phone
            contact.email = input("Enter new email (or press enter to keep current): ") or contact.email
            contact.address = input("Enter new address (or press enter to keep current): ") or contact.address
            print("Contact updated successfully!")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

    def delete_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the number of the contact to delete: ")) - 1
            contact = self.contacts.pop(index)
            print(f"{contact.name} has been deleted.")
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")

def main():
    manager = ContactManager()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
