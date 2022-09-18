import random
import re
# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('str_for_less_5/text5.1.txt', 'w+', encoding='utf-8') as f:
    line = []
    while True:
        li = input('Введите строку или пробел')
        if li == ' ' or li == '':
            f.writelines(line)
            break
        line.append(li + '\n')
    f.seek(0)
    print('Получилось', f.read())

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('str_for_less_5/text5.2.txt', 'r', encoding='utf-8') as f:
    i = 1
    for line in f:
        li = line.split()
        print(f'В строке {i} из {len(f)} {len(li)} слов')
        i += 1
print(f'Всего {i} строк')

# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
with open('str_for_less_5/text5.3.txt', 'r', encoding='utf-8') as f:
    i = 0
    average = 0
    low_salary = []
    for line in f:
        try:
            li = line.split()
            if int(li[1]) < 20000:
                low_salary.append(li[0])
            average += int(li[1])
            i += 1
        except ValueError:
            print('Ошибка в данных файла')
print('Низкооплачиваемые: ', low_salary)
print('Средняя зп по заводу: ', average / i)

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
    'Zero': 'Ноль'
}
li = []
with open('str_for_less_5/text5.4.txt', 'r', encoding='utf-8') as f:
    for line in f:
        li.append(line)
    print(li)
    for i in range(len(li)):
        line = li[i].split()
        if bool(dict[line[0]]):
            li[i].replace(dict[line[0]], line[0])
        li[i] += '\n'
with open('str_for_less_5/text5.4.1.txt', 'w+', encoding='utf-8') as f:
    f.writelines(li)
    f.seek(0)
    print('done', f.read(),)



# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open('str_for_less_5/text5.5.txt', 'w+', encoding='utf-8') as f:
    rand_numb = [str(random.randint(0, 999999)) + '\n' for i in range(20)]
    f.writelines(rand_numb)
    f.seek(0)
    sums = 0
    for line in f:
        sums += int(line)
print('Сумма чисел: ', sums)

#6 (Дополнительно). Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет
# и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

with open('str_for_less_5/text5.6.txt', 'r', encoding='utf-8') as f:
    numbs = []
    dict = {}
    for line in f:
        su = 0
        arr = line.split()
        numbs = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
        for i in numbs:
            su += i
        dict[arr[0]] = su
    print(dict)


#7 (Дополнительно) . Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет'
# содержать данные о фирме: название, форма собственности, выручка, издержки.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь
# (со значением убытков).

with open('str_for_less_5/text5.7.txt', 'r', encoding='utf-8') as f:
    firms = []
    dict_profit = {}
    dict_lesion = {}
    profit = 0
    lesion = 0
    sum_profit = 0
    sum_lesion = 0
    numbs = []
    for line in f:
        su = 0
        arr = line.split()
        numbs = [int(s) for s in re.findall(r'-?\d+\.?\d*', line)]
        print('числа', numbs)
        if numbs[0] > numbs[1]:
            profit += 1
            sum_profit += numbs[0]
            dict_profit[arr[0]] = numbs[0] - numbs[1]
        else:
            lesion += 1
            sum_lesion += numbs[0]
            dict_lesion[arr[0]] = numbs[0] - numbs[1]
    dict_profit['average_profit'] = sum_profit/profit
    dict_lesion['average_lesion'] = sum_lesion/lesion
    firms.append(dict_profit)
    firms.append(dict_lesion)
print('Done', firms)
