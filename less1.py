# 1
val_int = 1
val_str = 'str'
print(val_int, val_str)
user_str = str(input('str'))
user_int = int(input('int'))
print('user data:', user_int, user_str)

# 2
sec = int(input('#2 seconds'))
min = sec // 60
hours = min // 60
print('your time is : {}:{}:{}'.format(hours, min - hours * 60, sec - min * 60))

# 3
number = input('#3 number')
print('#3', int(number) + int(number * 2) + int(number * 3))

# 4
numb = input('sel numb')
count = 0
maxN = -1
while count < len(numb):
    if int(numb[count]) > maxN:
        maxN = int(numb[count])
    count += 1
print('Max', maxN)

# 5
revenue = int(input('Введите выручку'))
costs = int(input('Введите издержки'))

if revenue > costs:
    print('У вас есть прибыль, поздравляю! ')
else:
    print('Вы работаете в убыток :(')

# 6
if revenue > costs:
    personal = int(input('Сколько у вас персонала?'))
    print('Прибыль на одного сотрудника', (revenue - costs)/personal)

# 7
a, b = map(int, input('введите два числа через пробел').split())
if a >= b:
    print('спортсмен уже пробежал больше чем планировалось')
count = 1
while a <= b:
    a += a/10
    count += 1
    if a >= b:
        print('на', count, 'день спортсмен достиг результата — не менее', round(a, 3), 'км.')
        break

