# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0, 56 -> 11


# print('Введите число')
# a = input()
# sum = 0
# lenght = len(a)
# for i in range(lenght):
#     if a[i] != ',' and a[i] != '.' and a[i] != ' ':
#         sum = sum + int(a[i])
# print(sum)

###############################################################################################################
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

# number_N = int(input('введите число N:'))
# a = 1
# for i in range(number_N):
#     a = a * (i+1)
#     print(a, end=' ')

####################################################################################################################

# Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.

# numbers = int(input('Введите число n: '))
# list_numbers = []
# sum_elements = 0
# for n in range(1, numbers+1):
#     a = round((1 + 1 / n) ** n, 2)
#     sum_elements = sum_elements + a
#     list_numbers.insert(n, a)
# print(list_numbers)
# print('Сумма элементов полученной последовательности', sum_elements)

# 33

# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint


def create_rnd_list(n):
    rnd_list = [randint(-n, n) for i in range(n)]
    return rnd_list


def create_file_position(n):
    amount = randint(1, n)
    data = open('file.txt', 'w')
    for i in range(amount):
        a = randint(1, n)
        data.write(str(a)+"\n")


number = int(input('Введите число N: '))
list = create_rnd_list(number)
create_file_position(number)

p = 1
with open(r"file.txt", "r") as position_file:
    print('Позиции из файла file.txt')
    for i in position_file:
        print(i, end='')
        pp = int(i)
        p *= list[pp-1]
print('Сгенерированый список', list)
print('Произведения чисел ', p)
