from src.contact import ContactManager
from src.ui_operations import UIOperations


class ConsoleUI:
    """
    Пользовательский интерфейс командной строки для управления контактами.
    """

    def __init__(self, contact_manager: ContactManager):
        """
        Инициализирует новый экземпляр класса ConsoleUI.

        Args:
            contact_manager (ContactManager): Менеджер контактов для управления контактами.
        """
        self.contact_manager = contact_manager

    def run(self):
        """
        Запускает пользовательский интерфейс командной строки.
        """
        while True:
            print("\n1. Вывод записей")
            print("2. Добавление новой записи")
            print("3. Редактирование записи")
            print("4. Поиск записей")
            print("5. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                UIOperations.display_contacts(self.contact_manager)

            elif choice == "2":
                UIOperations.add_contacts(self.contact_manager)

            elif choice == "3":
                UIOperations.edit_contact(self.contact_manager)

            elif choice == "4":
                UIOperations.search_contacts(self.contact_manager)

            elif choice == "5":
                break

            else:
                print("Некорректный ввод. Попробуйте снова.")
