from src.contact import Contact


class UIOperations:
    """
    Операции пользовательского интерфейса для взаимодействия с контактами.
    """

    @staticmethod
    def display_contacts(contact_manager):
        """
        Выводит список контактов на экран с возможностью пагинации.

        Args:
            contact_manager: Менеджер контактов для управления контактами.
        """
        try:
            page_num = int(input("Введите номер страницы "))
            page_size = int(input("Введите количество элементов на  странице "))
        except ValueError:
            print("Ошибка: Введено некорректное значение. Введите целое число.")
            return

        contacts = contact_manager.display_contacts(page_num, page_size)
        for contact in contacts:
            print(contact.__dict__)

    @staticmethod
    def add_contacts(contact_manager):
        """
        Запрашивает информацию о новом контакте и добавляет его в телефонный справочник.

        Args:
            contact_manager: Менеджер контактов для управления контактами.
        """
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        organization = input("Введите название организации: ")
        work_phone = input("Введите рабочий телефон: ")
        personal_phone = input("Введите личный телефон: ")
        contact = Contact(
            last_name, first_name, middle_name, organization, work_phone, personal_phone
        )
        contact_manager.add_contact(contact)

    @staticmethod
    def edit_contact(contact_manager):
        """
        Запрашивает информацию о контакте для редактирования и вносит изменения в телефонный справочник.

        Args:
            contact_manager: Менеджер контактов для управления контактами.
        """
        try:
            contact_id = int(input("Введите номер контакта для редактирования: "))
        except ValueError:
            print("Ошибка: введено некорректное значение.Введите целое число.")
            return
        last_name = input("Введите фамилию: ")
        first_name = input("Введите имя: ")
        middle_name = input("Введите отчество: ")
        organization = input("Введите название организации: ")
        work_phone = input("Введите рабочий телефон: ")
        personal_phone = input("Введите личный телефон: ")
        contact = Contact(
            last_name, first_name, middle_name, organization, work_phone, personal_phone
        )
        contact_manager.edit_contact(contact_id, contact)

    @staticmethod
    def search_contacts(contact_manager):
        """
        Запрашивает критерии поиска и выводит результаты на экран.

        Args:
            contact_manager: Менеджер контактов для управления контактами.
        """
        key = input(
            "Введите название поля для поиска"
            "(last_name,first_name,middle_name,organization,work_phone,personal_phone): "
        ).lower()
        if key not in ["last_name","first_name","middle_name","organization","work_phone","personal_phone"]:
            print("Некорректно введено название поля для поиска")
            return
        value = input("Введите значение поля: ").lower()
        search_results = contact_manager.search_contacts(**{key: value})
        if search_results:
            for result in search_results:
                print(result)
        else:
            print("Запись не найдена.")
