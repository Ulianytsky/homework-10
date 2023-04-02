from ex01 import Garage, Car, Mark, RegNumber


garage = Garage()


def add_car(*args):
    mark = Mark(args[0])
    reg_num = RegNumber(args[1])
    car = Car(mark, reg_num)
    garage.add_car(car)
    return f"Car {args[0]} add successful"


def main():
    while True:
        user_input = input(">>>")

        if user_input.startswith("add"):
            model, reg_num = user_input.replace("add", '').strip().split()
            print(add_car(model, reg_num))

        if user_input.startswith("exit"):
            print("Bye")
            break

        # print("Unknown command, try again")


if __name__ == '__main__':
    print(garage)
    main()
    print(garage)
