from collections import UserDict


class Field:

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):

    def __init__(self, value):
        self.value = value


class Phone(Field):

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value


class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):

        self.phones.append(phone)

    def remove_phone(self, phone):

        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):

        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone


class AdressBook(UserDict):

    def add_record(self, record):

        self.data[record.name.value] = record
