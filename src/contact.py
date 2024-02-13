from typing import List, Any
import csv

from src.validators import (
    validate_at_least_one_name_field,
    is_unique_personal_phone_number,
    validate_work_phone,
    validate_personal_phone,
)


class Contact:
    """
    Представляет запись телефонного справочника.

    Атрибуты:
        last_name (str): Фамилия контакта.
        first_name (str): Имя контакта.
        middle_name (str): Отчество контакта.
        organization (str): Организация, к которой принадлежит контакт.
        work_phone (str): Рабочий телефон контакта.
        personal_phone (str): Личный телефон контакта.
    """

    def __init__(
        self,
        last_name: str,
        first_name: str,
        middle_name: str,
        organization: str,
        work_phone: str,
        personal_phone: str,
    ):
        """
        Инициализирует новый экземпляр класса Contact.

        Args:
            last_name (str): Фамилия контакта.
            first_name (str): Имя контакта.
            middle_name (str): Отчество контакта.
            organization (str): Организация, к которой принадлежит контакт.
            work_phone (str): Рабочий телефон контакта.
            personal_phone (str): Личный телефон контакта.
        """
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.organization = organization
        self.work_phone = work_phone
        self.personal_phone = personal_phone

    def __str__(self):
        """
        Возвращает строковое представление контакта.

        Returns:
            str: Строковое представление контакта.
        """
        return f"Контакт: {self.first_name} {self.last_name} {self.middle_name} {self.organization} {self.work_phone} {self.personal_phone}"


class ContactRepository:
    """
    Обрабатывает загрузку и сохранение контактов.
    """

    def __init__(self, filepath: str):
        """
        Инициализирует новый экземпляр класса ContactRepository.

        Args:
            filepath (str): Путь к файлу для хранения контактов.
        """
        self.filepath = filepath

    def load_contacts(self) -> List[Contact]:
        """
        Загружает контакты из телефонного справочника.

        Возвращает:
            List[Contact]: Список контактов, загруженных из репозитория.
        """
        contacts = []
        try:
            with open(self.filepath, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    contact = Contact(
                        row["last_name"],
                        row["first_name"],
                        row["middle_name"],
                        row["organization"],
                        row["work_phone"],
                        row["personal_phone"],
                    )
                    contacts.append(contact)

        except Exception as e:
            print("Произошла ошибка при загрузке контактов:", e)
        return contacts

    def save_contact(self, contacts: List[Contact]):
        """
        Сохраняет контакты в телефонном справочнике.

        Args:
            contacts (List[Contact]): Список контактов для сохранения.
        """
        try:
            with open(self.filepath, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = [
                    "last_name",
                    "first_name",
                    "middle_name",
                    "organization",
                    "work_phone",
                    "personal_phone",
                ]
                writer = csv.DictWriter(csvfile, fieldnames)
                for contact in contacts:
                    writer.writerow(
                        {
                            "last_name": contact.last_name,
                            "first_name": contact.first_name,
                            "middle_name": contact.middle_name,
                            "organization": contact.organization,
                            "work_phone": contact.work_phone,
                            "personal_phone": contact.personal_phone,
                        }
                    )
        except Exception as e:
            print("Произошла ошибка при сохранении контактов:", e)


class ContactManager:
    """
    Управляет записями в телефонном справочнике, включая их выыод на экран, добавление, редактирование и поиск.
    """

    def __init__(self, repository: ContactRepository):
        """
        Инициализирует новый экземпляр класса ContactManager.

        Аргументы:
            repository (ContactRepository): Репозиторий для хранения контактов.
        """
        self.repository = repository
        self.contacts = self.repository.load_contacts()

    @staticmethod
    def validate_contact(contact: Contact, contacts: List[Contact]) -> bool:
        """
        Проверяет корректность контакта.

        Args:
            contact (Contact): Контакт для проверки.
            contacts (List[Contact]): Список контактов для сравнения.

        Returns:
            bool: True, если контакт проходит все проверки, иначе False.
        """

        if not validate_at_least_one_name_field(contact):
            print(
                "Ошибка: хотя бы одно из полей last_name, first_name, middle_name должно быть заполнено."
            )
            return False

        if contact.personal_phone and not is_unique_personal_phone_number(contact.personal_phone, contacts):
            print("Ошибка: личный номер телефона не уникален.")
            return False

        if contact.work_phone and not validate_work_phone(contact.work_phone):
            print("Ошибка: некорректный рабочий номер телефона.")
            return False

        if contact.personal_phone and not validate_personal_phone(
            contact.personal_phone
        ):
            print("Ошибка: некорректный личный номер телефона.")
            return False

        return True

    def display_contacts(self, page_num: int, page_size: int) -> List[Contact]:
        """
        Возвращает список контактов с пагинацией.

        Аргументы:
            page (int): Номер страницы.
            page_size (int): Количество контактов на странице.

        Возвращает:
            List[Contact]: Список контактов для указанной страницы.
        """

        start_index = (page_num - 1) * page_size
        end_index = start_index + page_size
        contacts_to_display = self.contacts[start_index:end_index]
        if not contacts_to_display:
            print(f"На указанной странице контактов не найдено")
        return contacts_to_display

    def add_contact(self, contact: Contact):
        """
        Добавляет новый контакт.

        Аргументы:
            contact (Contact): Контакт для добавления.
        """
        if self.validate_contact(contact, self.contacts):
            self.contacts.append(contact)
            self.repository.save_contact(self.contacts)
            print("Контакт успешно добавлен")

    def edit_contact(self, contact_id: int, contact: Contact):
        """
        Редактирует существующий контакт.

        Args:
            contact_id (int): Индекс контакта для редактирования.
            contact (Contact): Обновленная информация о контакте.
        """

        if 0 < contact_id <= len(self.contacts):

            if self.validate_contact(contact, self.contacts):
                self.contacts[contact_id - 1] = contact
                self.repository.save_contact(self.contacts)
                print("Контакт успешно отредактирован")
        else:
            print("Контакта с данным номером не существует.")

    def search_contacts(self, **kwargs: Any) -> List[Contact]:
        """
        Выполняет поиск контактов по заданным критериям.

        Ключевые аргументы:
            Любой именованный аргумент может быть использован для фильтрации контактов.

        Возвращает:
            List[Contact]: Список контактов, соответствующих критериям поиска.
        """

        search_results = []

        for contact in self.contacts:
            match = True
            for key, value in kwargs.items():
                if getattr(contact, key, None).lower() != value:
                    match = False
                    break
            if match:
                search_results.append(contact)
        return search_results
