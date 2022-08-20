'''
Задание 1
'''

import sys

f_obj, name_v< rate_v, hours_v = sys.argv
print(f_obj)
def calc_salary(rate, hours):
    try:
        print(f'Работник {name_v} заработал {int(rate)} * int(hours) * 1.25}')
    except:
        print("Не правильный тип данных")
        exit()
calc_salary(rate_v, hours_v)







'''
Задание 2
'''
from random import randint


primary_list = [randint(0, 51) for i in range(20)]
list_2 = [primary_list[el]
    for el in range(1, len(primary_list))
    if primary_list[el] > primary_list[el-1]]

print(list_2)


'''
Задание 3
'''

print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])


'''
Задание 4
'''

primary_list = [randint(0, 36) for i in range(20)]
result_list = [el for el in primary_list if primary_list.count(el) == 1]
print(result_list)


'''
Задание 5
'''

from funvtools import reduce

primary_list = [i for i in range(100, 10001, 2)]
print(primary_list)
result = reduce(lambda item, item2: item * item2, primary_list)
print(result)


'''
Задание 6
'''
from itertools import count, cycle

list_int = []

a = int(input("Введите первое число: "))
b = int(input("Введите последнее число: "))

for i in count(a):
    if i > b:
        break
    print(i)
    list_int.append(i)

print(" ")

print(list_int)
count = 0
for item in cycle(list_int):
    if count >= len(list_int):
        break
    print(item)
    count += 1


'''
Задание 7
'''

from itertools import count

def factorial(x):
    fact = 1
    for i in count(1):
        if x > i:
            break
        fact = fact * i
        yield fact

x = int(input("Введите число: "))
i = 0
for el in factorial(x):
    ++i
    print(f"!{i} = {el}")