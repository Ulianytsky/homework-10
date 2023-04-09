from collections import UserDict


class Field:
    def __init__(self):
        self.__value = None

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.__value == other.__value


class Name(Field):
    def __init__(self, name):
        super().__init__()
        self.__value = name.strip()


class Phone(Field):
    def __init__(self, phone):
        super().__init__()
        self.__value = self.format_phone(phone)

    def format_phone(self, phone):
        return ''.join(filter(str.isdigit, phone))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        phone = self.__value
        return f'+{phone[0]} ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:]}'


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone_index, new_phone):
        self.phones[phone_index] = Phone(new_phone)

    def delete_phone(self, phone_index):
        del self.phones[phone_index]

    def __str__(self):
        return f'{self.name}: {", ".join(str(phone) for phone in self.phones)}'


class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.__str__()] = record

    def delete(self, name):
        del self.data[name]

    def search(self, query):
        result = []
        for record in self.data.values():
            if record.name.__str__() == query:
                result.append(record)
            elif query in [phone.__str__() for phone in record.phones]:
                result.append(record)
        return result
