import time


# 1. Создать класс TrafficLight (светофор).
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.


class TrafficLight:
    __colour = 'red'

    def running(self):
        i = 0
        while i < 3:
            if self.__colour == 'red':
                print('Current colour', self.__colour)
                time.sleep(7)
                self.__colour = 'yellow'
            if self.__colour == 'yellow':
                print('Current colour', self.__colour)
                time.sleep(3)
                self.__colour = 'green'
            if self.__colour == 'green':
                print('Current colour', self.__colour)
                time.sleep(3)
                self.__colour = 'red'
            i += 1
        return f'На светофоре горит {self.__colour} цвет'


trafficLight = TrafficLight()
trafficLight.running()


# 2. Реализовать класс Road (дорога).

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculated(self, mass, thick):
        return self._length * self._width * mass * thick


road = Road(50, 100)
print(f"Нужно {road.calculated(60, 3)}т")


# 3. Реализовать базовый класс Worker (работник).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
        self.position = position

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


new_position = Position('Ivan', "Ivanov", "Driver", {"wage": 1000, "bonus": 150})
print(f'Полное имя {new_position.get_full_name()} заработал: {new_position.get_total_income()}')


# 4. Реализуйте базовый класс Car.
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.current_speed = 0

    def go(self):
        self.current_speed = self.speed
        return 'GO'

    def stop(self):
        self.current_speed = 0
        return 'STOP'

    def turn(self, direction):
        return f'{self.name} повернула в {direction} сторону'

    def show_speed(self):
        return f'Текущая скорость: {self.current_speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed

    def show_speed(self):
        if int(self.current_speed) > 60:
            return 'Вы Превысили скорость!'
        else:
            return f'Ваша скорость {self.current_speed}'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self.speed = speed

    def show_speed(self):
        if int(self.current_speed) > 40:
            return 'Вы Превысили скорость!'
        else:
            return f'Ваша скорость {self.current_speed}'


workCar = TownCar(60, 'red', 'Mazda', True)
print(workCar.show_speed())
print(workCar.go())
print(workCar.show_speed())
print(workCar.stop())
print(workCar.show_speed())


# 5. Реализовать класс Stationery (канцелярская принадлежность).

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self, speed):
        return speed


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self, speed):
        return f'эта {self.title} может писать {speed} слов в минуту'


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self, speed):
        return f'этот {self.title} может писать {speed} слов в минуту'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self, speed):
        return f'эта канцелярская пренадлежность под названием {self.title} может писать {speed} слов в минуту'


pen = Pen('ручка')
print(pen.draw(50))
pen = Pencil('карандаш')
print(pen.draw(70))
pen = Handle('маркер')
print(pen.draw(5))
