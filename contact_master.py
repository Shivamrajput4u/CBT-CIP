class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactMaster:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():  # Case-insensitive search
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted.")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():  # Case-insensitive search
                print(contact)
                return
        print(f"Contact '{name}' not found.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contact List:")
        for contact in self.contacts:
            print(contact)


def main():
    cm = ContactMaster()
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            cm.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name of contact to delete: ")
            cm.delete_contact(name)

        elif choice == '3':
            name = input("Enter name of contact to search: ")
            cm.search_contact(name)

        elif choice == '4':
            cm.display_contacts()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
