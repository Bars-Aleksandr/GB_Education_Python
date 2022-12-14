print('Hello world')
########################## Типы данных и переменная (Data types and variable) #################################
############################# int, float, boolean, str, list, none ############################################
# #
# a = 23
# b = 1.23
# val = None
# print(type(val))
# s = 'name'
# print(s)
# print(a, b, val, s)
# print(a, '-', b, '-', val, '-', s)
# print('{} - {} - {} - {}'.format(a, b, val, s))
# print('{3} - {2} - {1} - {0}'.format(a, b, val, s))
# print(f'{a} - {b} - {val} - {s}')
# print('-----------------------------------------------------')
# list = [1, 2, 3, 4, 'list', True] ############## ТАК ДЕЛАТЬ МОЖНО, НО НЕ НУЖНО
# print(list)


############################# Ввод и вывод данных #############################################
############################# Преобразование типов ############################################

# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b)
# print('{} -- {}'.format(a, b))
# print(a, ' + ', b, ' = ', a + b)
# ПОЛУЧИТСЯ СЛОЖЕНИЕ СТРОК НАПР. 3+5=35, Т.К. ПО УМОЛЧАНИЮ СТРОКИ
#####ДЛЯ ПОЛУЧЕНИЯ ЧИСЕЛ ПРИ ВВОДЕ###########################
# print('Введите а')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a + b)
# print('{} + {} = {}'.format(a, b, a + b))


################################################## Арифметические операции                                   #######
################################################## Важно и нужно, без них вы не напишете ни одной программы  #######
################################################## Если помните математику – проблем не будет                #######
################################################## +, -, * , /, %, //, **                                    #######
################################################## Приоритет операций  **, ⊕, ⊖,* , /, //, %, +, -         #######
################################################## ( ) Скобки меняют приоритет                               #######
# Сокращённые операции и операции присваивания
# Демонстрация
iter = 2
iter += 3  # iter = iter + 3
iter -= 4  # iter = iter - 4
iter *= 5  # iter = iter * 5
iter /= 5  # iter = iter / 5
iter //= 5  # iter = iter // 5  ЭТО ЦЕЛОЧИСЛЕННОЕ ДЕЛЕНИЕ
iter %= 5  # iter = iter % 5
iter **= 5  # iter = iter ** 5  ЭТО ВОЗВЕДЕНИЕ В СТЕПЕНЬ


################################################## Логические операции                  ###########
################################################## >, >=, <, <=, ==, !=                 ###########
################################################## not, and, or – не путать с &, |, ^   ###########
################################################## Кое-что ещё: is, is not, in, not in  ###########
# f = [1, 2, 4, 5]
# print(f)
# print(2 in f)  # True
# print(not 2 in f)  # false

# even = not f[2] % 2  # ПРОВЕРКА ЧЕТНОСТИ
# print(even)

#########################################  Управляющие конструкции: if , if-else ##########
# if condition:
#  # operator 1
#  # operator 2
#  # ...
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # ...
#  # operator n + m
# username = input('Введите имя: ')
# if (username == 'Маша'):
#     print('Ура, это же МАША!')
# else:
#     print('Привет, ', username)
# if condition1:
#  # operator
# elif condition2:
#  # operator
# elif condition3:
#  # operator
# else:
#  # operator


########################################### Управляющие конструкции: while ############
# while condition:
# operator 1
# operator 2       ОТСТУПЫ ВАЖНЫ
# . . .
# operator n

# while condition:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n
# else:
#  # operator n + 1
#  # operator n + 2
#  # . . .
#  # operator n + m

# original = 23456
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)  # ПЕРЕВОРАЧИВАЕТ ЧИСЛО
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)


############################################## Управляющие конструкции: for #################
# for i in enumeration:
#  # operator 1
#  # operator 2
#  # . . .
#  # operator n

# for i in 1, -2, 3, 14, 5:
# print(i)


############################################ Знакомьтесь – range ##################################
# r = range(5)  # range(0, 5) СПИСОК ОТ 1 .. 5
# for i in r:
#     print(i)
# r = range(2, 5)  # range(2, 5)
# for i in r:
#     print(i)
# r = range(-5, 0)  # range(-5, 0)
# r = range(1, 10, 2)  # range(1, 10, 2) СПИСОК ОТ 1 .. 9 ЧЕРЕЗ 2 [1 3 5 7 9]
# r = range(100, 0, -20)  # range(100, 0, -20)

############################################## Немного о строках ###################################
# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # 39
# print('ещё' in text)  # True
# print(text.isdigit())  # False
# print(text.islower())  # True
# print(text.replace('ещё', 'ЕЩЁ'))
# for c in text:
#  print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])  # c
# print(text[1])  # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])  # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2]  # ...


############################################### Список – пронумерованная, изменяемая коллекция ############
############################################### объектов произвольных типов                    ############
############################################### Списки: введение                               ############
# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i)  # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)                            # red green blue
# for e in colors:
#     print(e*2)                          # redred greengreen blueblue
# colors.append('gray')                   # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')                    # del colors[0] # удалить элемент


################################################ Функции                                          ########
################################################ Это фрагмент программы, используемый многократно ########

# def function_name(x):
# body line 1
# . . .
# body line n
# optional return

# def f(x):
#     return x**2


# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return


# print(f(1))                           # Целое
# print(f(2.3))                         # 23
# print(f(28))                          # None
# print(type(f(1)))                     # str
# print(type(f(2.3)))                   # int
# print(type(f(28)))                    # NoneType
