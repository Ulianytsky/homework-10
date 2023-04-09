from adressbook import Record, AdressBook, Phone
import re


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Print "help"'
    return inner


def help(*args):
    return '''How can I help you? For adding type add, name, " " and phone number'''


@input_error
def add(ab, *args):
    name, *phones = args[0].split()
    record = Record(name)
    for phone in phones:
        record.add_phone(phone)
    ab.add_record(record)
    return f'{name}, phone_number {phones} added to the address book.'


@input_error
def change(ab, *args):
    name, phone_index, new_phone = args[0].split()
    record = ab.data[name]
    record.edit_phone(int(phone_index) - 1, new_phone)
    return f'Changed phone number {phone_index} for {name} to {new_phone}.'


@input_error
def phone(ab, *args):
    query = args[0]
    result = ab.search(query)
    if result:
        return '\n'.join(str(record) for record in result)
    else:
        return f'Contact {query} does not exist in the list.'


def show_all(ab, *args):
    if not ab.data:
        return 'There are no contacts in the list.'
    output = ''
    for record in ab.data.values():
        output += str(record) + '\n'
    return output
