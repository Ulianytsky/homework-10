from collections import UserDict


class Field:
    def __init__(self, value=None):
        self.__value = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__value})"

    def __str__(self):
        return str(self.__value)

    def __eq__(self, other):
        if isinstance(other, Field):
            return self.__value == other.__value
        return self.__value == other


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, phone_index, new_phone):
        self.phones[phone_index] = new_phone

    def delete_phone(self, phone_index):
        del self.phones[phone_index]


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record
