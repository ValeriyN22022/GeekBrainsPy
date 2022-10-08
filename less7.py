from abc import ABC, abstractmethod


# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.


class Matrix:
    def __init__(self, li):
        self.lists = li

    def __str__(self):
        for i in range(len(self.lists)):
            print(str(self.lists[i]), end='\n')

    def __add__(self, other):
        new_matrix = []
        try:
            if len(self.lists) <= len(other.lists):
                for i in range(len(self.lists)):
                    new_line = []
                    for j in range(len(self.lists[i])):
                        new_line.append(int(self.lists[i][j]) + int(other.lists[i][j]))
                    new_matrix.append(new_line)
            else:
                for i in range(len(other.lists)):
                    new_line = []
                    for j in range(len(other.lists[i])):
                        new_line.append(int(self.lists[i][j]) + int(other.lists[i][j]))
                    new_matrix.append(new_line)
            return new_matrix
        except TypeError:
            print('Не тот тип')


matr = Matrix([[1, 2, 4, 5, 6],
               [2, 3, 4, 5, 6],
               [7, 56, 45, 3, 223],
               [45, 54, 546, 76, 87]])
matr2 = Matrix([[1, 2, 4, 5, 6],
                [1, 1, 1, 1, 1],
                [7, 56, 5, 3, 223],
                [45, 4, 6, 6, 87]])
print(matr + matr2)
print(matr)


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.

class SuitAbstract(ABC):
    def __init__(self, height):
        self.height = height

    @abstractmethod
    def material(self):
        return self.height * 2 + 0.3


class CoatAbstract(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def material(self):
        return self.size / 6.5 + 0.5


class Clothes:
    def material(self):
        return 'Вы забыли прописать отдельный метод для одной из одежд'

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property()
    name = name.setter(set_name)
    name = name.getter(get_name)


class Coat(Clothes, CoatAbstract):

    def __init__(self, name, size):
        super(Coat, self).__init__(name)
        self.size = size


class Suit(Clothes, SuitAbstract):

    def __init__(self, name, height):
        super(Suit, self).__init__(name)
        self.height = height

    def material(self):
        return self.height * 2 + 0.3


clothes = Clothes('Одежда')
coat = Coat('Пальто', 123)
print(coat.material())
suit = Suit('Костюм', 345)


# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    try:
        def __init__(self, number_of_cells):
            self.number_of_cells = int(number_of_cells)
    except ValueError:
        print('НЕ тот тип')

    def __add__(self, other):
        return self.number_of_cells + other.number_of_cells

    def __mul__(self, other):
        return self.number_of_cells * other.number_of_cells

    def __truediv__(self, other):
        return self.number_of_cells // other.number_of_cells

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells <= 0:
            return 'Разность клеток меньше или равна нулю, вычитать нечего'
        else:
            return self.number_of_cells - other.number_of_cells

    def make_order(self, row):
        li = ''
        for i in range(self.number_of_cells // row):
            for j in range(row + 1):
                # counter += 1
                if j != row:
                    li += '*'
                else:
                    li += '\n'
                    # counter = 0
        if self.number_of_cells % row != 0:
            for i in range(self.number_of_cells % row):
                li += '*'
        return li


cell = Cell(123)
cell2 = Cell(126)
print(cell - cell2)
print(cell.make_order(10))
