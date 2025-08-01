import json
from rich.console import Console
from contact import Contact


class ContactBook:

    def __init__(self):
        self.console = Console()
        self.contacts: list[Contact] = []

    def load_contacts(self):
        with open('contacts.json') as jsonfile:
            data_list = json.load(jsonfile)

        for data in data_list:
            self.contacts.append(Contact.from_dict(data))

    def save_contacts(self):
        data = []
        for contact in self.contacts:
            data.append(contact.to_dict())

        with open('contacts.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

    def print_menu(self):
        self.console.print('[bold italic yellow on red blink]\n======== Menu ========')
        self.console.print(
            '1. Add New Contact\n'
            '2. Show All Contacts\n'
            '3. Search Contact\n'
            '4. Update Contact\n'
            '5. Delete Contact\n'
            '6. Exit\n'
        )

    def add_contact(self):
        self.console.print("[bold green]Enter A New Contact Information")
        name = input("Name: ").strip().title()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()

        self.load_contacts()
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()

    def print_contacts(self):
        pass

    def remove_contact(self):
        pass

    def update_contact(self):
        pass

    def search_contact(self):
        pass

    def run(self):
        print("salom, Contact Book Projectga Xush Kelibsiz!")
        while True:
            self.print_menu()

            choice = input("> ")
            if choice == '1':
                self.add_contact()
            
