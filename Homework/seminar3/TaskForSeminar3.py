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
# print()
# print(sum)
#################################################################################
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def create_rnd_list(n):
    rnd_list = [randint(1, n) for i in range(n)]
    return rnd_list


n = int(input('Enter the number of list items: '))
list = create_rnd_list(n)
print('My list: ', list)

lst_multiple = []
i = 0
while i <= (n-1)-i:
    lst_multiple.append(list[i] * list[n-1-i])
    i += 1
print('Multiple list: ', lst_multiple)
