
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color



    def print_info(self):
        print(f"Модель: {self.__model}")
        print(f"Мощность: {self.__engine_power} л.с.")
        print(f"Цвет: {self.__color}")
        print(f"Владелец: {self.owner}")

    def model(self):
        return self.__model

    def engine_power(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        new_color_low = new_color.lower()
        if new_color_low in [color.lower() for color in Vehicle.__COLOR_VARIANTS]:
            self.__color = Vehicle.__COLOR_VARIANTS[
                [color.lower() for color in Vehicle.__COLOR_VARIANTS].index(new_color_low)]
            print(f"Цвет успешно изменен на {self.__color}.")
        else:
            print(f"Нельзя сменить цвет на {new_color}.")


class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power, __PASSENGERS_LIMIT=5):
        super().__init__(owner, model, color, engine_power)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
