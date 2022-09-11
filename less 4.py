import random
from functools import reduce
from itertools import cycle, count


# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
# значений необходимо запускать скрипт с параметрами.


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.

def prev_list():
    li = [random.randint(0, 999999) for i in range(20)]
    big_li = []
    print('исходный список ', li)
    for i in range(1, len(li)):
        if li[i - 1] < li[i]:
            big_li.append(li[i])
    return big_li


print('оформатированный список: ', prev_list())

# 3 Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.

print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])


# 4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел,
# соответствующих требованию. Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

def repeating_numbers():
    li = [random.randint(0, 99) for i in range(200)]
    no_rep_li = []
    print('исходный список ', li)
    for i in range(1, len(li)):
        if li.count(li[i]) == 1:
            no_rep_li.append(li[i])
    return no_rep_li


print('оформатированный список: ', repeating_numbers())

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа
# от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.

print(reduce(lambda x, y: x + y, [i for i in range(100, 1001)]))

# 6. Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.

li = [i for i in range(int(input('Введите начало списка')), int(input('Введите конец')))]
print('без библиотек ', li)
a = int(input('Введите начало списка'))
b = int(input('Введите конец'))
for i in count(a):
    if i > b:
        break
    print(i)

i = 0
for el in cycle(li):
    i += 1
    if i >= 30:
        break
    print(el)

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа. В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

n = int(input('введите последнее число для факториала'))

pref_fact = 1
count = 1


def fact(n,):
    for i in range(1, n + 1):
        print('dd', pref_fact, i, pref_fact * i)
        yield pref_fact * i


for el in fact(n):
    print(f'Факториал {count}! ===', el)
    count += 1
    pref_fact = el