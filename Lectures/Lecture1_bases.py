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
