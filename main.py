'''
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
'''
# with open('new_file.txt', 'w') as f_obj:
#     a = 'some text'
#     while a != '':
#         a = input("Введите строку: ")
#         if a == "":
#             break
#         f_obj.write(f"{a}\n")
import random

'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
'''
# with open('new_file.txt', 'r') as f_obj:
#     lines = 0
#     words = 0
#     for i in f_obj:
#         lines += 1
#         words += len(i.split())
#     print(f'lines = {lines}\n words = {words}')

'''
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
# with open('new_file.txt', 'r+') as f_obj:
#     for i in range(1, 3):
#         surname = input("Введите фамилию сотрудника: ")
#         salary = float(input("Введите величину оклада: "))
#         f_obj.write(f'{surname} {salary}\n')
#
# with open('new_file.txt', 'r+') as f_obj:
#     new_list = [row.strip() for row in f_obj]
#     sn_list = []
#     sl_list = []
#     for i in range(len(new_list)):
#         bubble_list = new_list[i].split()   # я решил сделать с помощью метода "пузырька"
#         sn_list.append(bubble_list[0])      # знаю, что можно сделать проще, а не плодить код
#         sl_list.append(bubble_list[1])
#     average = 0
#     for i in range(len(sl_list)):
#         average += float(sl_list[i])
#         if float(sl_list[i]) < 20000:
#             print(f'{sn_list[i]}\n')
#     average = average/len(sl_list)
#     print(f'Среднее значение дохода: {average}')


'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.

'''
# new_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# word_list = []
# with open('number_4.txt', 'r', encoding="utf-8") as f_obj:
#
#     for i in f_obj:
#         bubble_list = i.split()
#         for j in bubble_list:
#             word_list.append(j)
#     print(word_list)
#     for i in range(len(word_list)):
#         try:
#             word_list[i] = (new_dic[word_list[i]])
#
#         except Exception:
#             continue
#
# with open('number_4_edit.txt', 'w') as f_obj:
#     for i in word_list:
#         try:
#             a = int(i)
#             f_obj.write(f'{i}\n')
#         except Exception:
#             f_obj.write(f'{i} ')

'''
 Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

'''
# with open('ex5.txt', 'w') as f_obj:
#     for i in range(11):
#         f_obj.write(f'{random.randint(0, 101)} ')
# with open('ex5.txt', 'r') as f_obj:
#     new_list = f_obj.readline().split()
#     int_sum = 0
#     for i in new_list:
#         int_sum += int(i)
#     print(int_sum)

'''
Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
with open('ex6.txt', 'r', encoding="utf-8") as f_obj:
    string_list = f_obj.read().split('\n')[:-1]
    new_dict = dict()
    for i in string_list:
        key = i.split()[0]
        value = i.split()[1:]
        new_dict[key] = value
print(new_dict)
