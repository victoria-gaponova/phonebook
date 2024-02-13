import re


def validate_at_least_one_name_field(entry) -> bool:
    """
    Проверяет, что хотя бы одно из полей last_name, first_name или middle_name заполнено.

    Args:
        entry: Контакт для проверки.

    Returns:
        bool: True, если хотя бы одно поле заполнено, иначе False.
    """
    return bool(entry.last_name or entry.first_name or entry.middle_name)


def is_unique_personal_phone_number(phone_number, entries) -> bool:
    """
    Проверяет уникальность персонального номера телефона среди списка контактов.

    Args:
        phone_number (str): Номер телефона для проверки.
        entries: Список контактов для сравнения.

    Returns:
        bool: True, если номер уникален, иначе False.
    """
    return all(phone_number != entry.personal_phone for entry in entries)


def validate_work_phone(phone_number: str) -> bool:
    pattern = r"^[1-9][0-9]{5}$"
    return re.match(pattern, phone_number) is not None


def validate_personal_phone(phone_number: str) -> bool:
    pattern = r"^\+[1-9][0-9]{10,11}$"
    return re.match(pattern, phone_number) is not None
