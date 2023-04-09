from adressbook import AdressBook, Record, Name, Field


contacts = AdressBook()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Print "help"'
    return inner


def help(*args):
    return '''How can I help you? For adding type add, name, and phone number.
To change phone number type change, name, and phone number.
To find a phone number type phone and name.
To show all contacts type show all.
To exit type exit.
'''


@input_error
def add(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = list_of_param[1:]
    if not phone_number:
        raise IndexError()
    record = Record(Name(name))
    for number in phone_number:
        record.add_phone(Field(number))
    contacts.add_record(record)
    return f'{name}, phone number {phone_number} added'


@input_error
def change(*args):
    list_of_param = args[0].split()
    name = list_of_param[0]
    phone_number = list_of_param[1:]
    if not phone_number:
        raise IndexError()
    if name not in contacts:
        return f'Contact {name} does not exist in the list.'
    record = contacts[name]
    record.phones.clear()
    for number in phone_number:
        record.add_phone(Field(number))
    return f'Changed phone number for {name} to {phone_number}'


@input_error
def phone(*args):
    name = args[0]
    if name not in contacts:
        return f'Contact {name} does not exist in the list.'
    record = contacts[name]
    phone_numbers = ", ".join(str(phone) for phone in record.phones)
    return f'Phone number for {name}: {phone_numbers}'


def show_all(*args):
    if not contacts:
        return 'There are no contacts in the list.'
    output = ''
    for record in contacts.values():
        phone_numbers = ", ".join(str(phone) for phone in record.phones)
        output += f'{record.name}: {phone_numbers}\n'
    return output


def exit(*args):
    return 'Bye!'


def no_command(*args):
    return 'Unknown command, try again.'


COMMANDS = {
    help: 'help',
    add: 'add',
    change: 'change',
    phone: 'phone',
    show_all: 'show all',
    exit: 'exit'
}


def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, '').strip()
    return no_command, None


def main():
    print(help())
    while True:
        user_input = input('>>>')
        command, data = command_handler(user_input)
        print(command(data))
        if command == exit:
            break


if __name__ == '__main__':
    main()
