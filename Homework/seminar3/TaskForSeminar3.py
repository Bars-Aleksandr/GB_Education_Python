# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# from random import randint


# def create_rnd_list(n):
#     rnd_list = [randint(1, n) for i in range(n)]
#     return rnd_list


# n = int(input('Enter the number of list items: '))
# list = create_rnd_list(n)
# print('My list: ', list)
# sum = 0
# for i in range(1, len(list), 2):
#     sum += list[i]
# print('Summa elements:', sum)
#################################################################################
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# def create_rnd_list(n):
#     rnd_list = [randint(1, n) for i in range(n)]
#     return rnd_list


# n = int(input('Enter the number of list items: '))
# list = create_rnd_list(n)
# print('My list: ', list)

# lst_multiple = []
# i = 0
# while i <= (n-1)-i:
#     lst_multiple.append(list[i] * list[n-1-i])
#     i += 1
# print('Multiple list: ', lst_multiple)
###############################################################################################
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# import random


# def create_rnd_list(n):
#     rnd_list = [round(random.uniform(1, n), 2) for i in range(n)]
#     return rnd_list


# def fraction(x): return x % 1


# #n = int(input('Enter the number of list items: '))
# n = 5
# list = create_rnd_list(n)
# print('My list: ', list)
# list2 = sorted([round(fraction(list[i]), 2) for i in range(n)])
# print(list2)
# print(list, '=>', round(list2[n-1]-list2[0], 2))
##################################################################################################
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def dec_in_bin(num):
    bin = ''
    while num != 0:
        bin = bin + str(num % 2)
        num = num // 2
    bin = bin[::-1]
    return bin


def invert1_0(bin):
    temp = list(bin)
    for i in range(len(temp)):
        if temp[i] == '0':
            temp[i] = '1'
        else:
            temp[i] = '0'
    bin = ''.join(temp)
    return bin


dec = int(input('Enter a Number in DEC format: '))
if dec >= 0:
    bin = dec_in_bin(dec)
else:
    bin = bin(dec)
print(dec, '->', bin)


#######################################################################################################

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# def negafibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return -1
#     else:
#         num1, num2 = 1, -1
#         for i in range(2, n):
#             num1, num2 = num2, num1 - num2
#         return num2


# number = int(input('Enter number: '))
# list1 = [fibonacci(i) for i in range(1, number + 1)]
# list2 = [negafibonacci(i) for i in range(number, 1, -1)]
# print(list2+list1)
