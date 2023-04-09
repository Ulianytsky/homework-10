from adressbook import AdressBook, Record, Name, Phone


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
def add(abook, *args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    record = Record(name)
    for phone in list_of_param[1:]:
        record.add_phone(Phone(phone))
    abook.add_record(record)
    return f'{name}, phones {record.phones}'


@input_error
def change(abook, *args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    record = abook.data.get(name)
    if record is None:
        return f'Contact {name} does not exist in the list.'
    for i, phone in enumerate(list_of_param[1:]):
        record.edit_phone(i, Phone(phone))
    return f'Changed phone numbers for {name} to {record.phones}'


def phone(abook, name):
    record = abook.data.get(Name(name))
    if record is None:
        return f'Contact {name} does not exist in the list.'
    return f'Phone numbers for {name}: {record.phones}'


def show_all(abook):
    if not abook.data:
        return 'There are no contacts in the list.'
    output = ''
    for name, record in abook.data.items():
        output += f'{name}: {record.phones}\n'
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


def command_handler(abook, text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            if kword == 'phone':
                return lambda: command(abook, text.replace(kword, '').strip())
            return lambda: command(abook, text.replace(kword, '').strip())
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
