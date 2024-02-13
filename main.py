from src.contact import ContactRepository, ContactManager
from src.user_interface import ConsoleUI

if __name__ == "__main__":
    repository = ContactRepository("phonebook.csv")
    contact_manager = ContactManager(repository)
    ui = ConsoleUI(contact_manager)
    ui.run()
