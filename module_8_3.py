class Car:

    def __init__(self, model, vin, numbers):
        self.model = str(model)
        self.__vin = vin
        self.__numbers = str(numbers)
        self.__is_valid_vin(vin_number=vin)
        self.__is_valid_numbers(numbers=numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int) or isinstance(vin_number, bool):
            raise IncorrectVinNumber(f'Некорректный тип vin номера')
        elif 1000000 > float(vin_number):
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')
        elif 9999999 < float(vin_number):
            raise IncorrectVinNumber(f'Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f'Некорректный тип данных для номеров')
        elif 6 != len(numbers):
            raise IncorrectCarNumbers(f'Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')