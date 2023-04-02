from collections import UserDict


class Core:

    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Mark(Core):
    pass


class Model(Core):
    pass


class RegNumber(Core):
    pass


class Mileage(Core):
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError('Must be a integer')
        self.value = value


class Car:

    def __init__(self,
                 mark: Mark,
                 model: Model,
                 reg_number: RegNumber,
                 mileage: Mileage = None):
        self.mark = mark
        self.model = model
        self.reg_number = reg_number
        self.mileages = []
        if mileage:
            self.mileages.append(mileage)

    def add_mileage(self, mileage: Mileage):
        max_mileage = max([m.value for m in self.mileages])
        if self.mileages and mileage.value < max_mileage:
            raise ValueError(f"Max mileage {max_mileage}")
        self.mileages.append(mileage)

    def change_reg_number(self, new_reg_num):
        old_reg_num = self.reg_number
        self.reg_number = new_reg_num
        return f"Change {old_reg_num} to {new_reg_num}"


class Garage(UserDict):

    def add_car(self, car: Car):
        self.data[car.mark.value] = car


if __name__ == '__main__':

    garage = Garage()

    mark = Mark("VW")
    model = Model("Passat")
    reg = RegNumber("AO5565AO")

    mil1 = Mileage(200000)
    mil2 = Mileage(300000)

    car1 = Car(mark, model, reg, mil1)

    print(f"{car1.model}: {car1.mark} - {car1.reg_number}")

    car2 = Car(Mark('Audi'), Model("A6"),
               RegNumber("AA1234AA"), Mileage(180000))

    garage.add_car(car1)
    garage.add_car(car2)

    car3 = garage.get('VW')

    if car3:
        car3.change_reg_number(RegNumber('BH3456BX'))

    for car in garage.values():
        print(f"{car.mark} {car.model} {car.reg_number}")
