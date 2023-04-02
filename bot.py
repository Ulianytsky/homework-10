from adress_book import AdressBook, Record, Name, PhoneNumber

adressbook = AdressBook()


def add_record(*args):
    name = Name(args[0])
    phone_num = PhoneNumber(args[1])
    record = Record(name, phone_num)
    adressbook.add_record(record)
    return f"Record {args[0]} add successful"



def main():
    print(help())
    while True:
        user_input = input(">>>")

        if user_input.startswith("add"):
            name, phone_num = user_input.replace("add", '').strip().split()
            print(add_record(name, phone_num))

        if user_input.startswith("exit"):
            print("Bye")
            break


if __name__ == '__main__':
    print(adressbook)
    main()
    print(adressbook)
