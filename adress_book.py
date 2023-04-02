from collections import UserDict


class Field:

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class PhoneNumber(Field):
    pass


class Record:

    def __init__(self,
                 name: Name,
                 phone_number: PhoneNumber):
        self.name = name
        self.phone_number = [phone_number]

    def add_phone_number(self, phone_number: PhoneNumber):
        self.phone_numbers.append(phone_number)

    def remove_phone_number(self, phone_number: PhoneNumber):
        if phone_number in self.phone_numbers:
            self.phone_numbers.remove(phone_number)
        else:
            raise ValueError(
                "The provided phone number does not exist for this record.")

    def change_phone_number(self, new_phone_num):
        old_phone_num = self.phone_number
        self.phone_number = new_phone_num
        return f"Change {old_phone_num} to {new_phone_num}"


class AdressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record


if __name__ == '__main__':

    adressbook = AdressBook()

    name = Name("John")
    phone_number1 = PhoneNumber("1234567")
    record1 = Record(name, phone_number1)
    print(f"{record1.name} - {record1.phone_number[0]}")

    record2 = Record(Name('Kolja'),
                     PhoneNumber("9876543"))
    print(f"{record2.name} - {record2.phone_number[0]}")

    adressbook.add_record(record1)
    adressbook.add_record(record2)
