# #  1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли
# #     этот день выходным.
# #     Пример:
# #     - 6 -> да
# #     - 7 -> да
# #     - 1 -> нет
# print('Введите день недели цифрой')
# weekend = int(input())
# if weekend in [6, 7]:
#     print(weekend, '->', 'да')
# else:
#     print(weekend, '->', 'нет')


# # 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             if (not (x or y or z) == (not x and not y and not z)):
#                 print('для аргументов', x, y, z, ' утверждение верно')
#             else:
#                 print('для аргументов', x, y, z, ' утверждение  неверно')


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
#    четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#      Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# print('Введите координату x')
# x = float(input())
# print('Введите координату y')
# y = float(input())
# if x > 0 and y > 0:
#     print(f'х = {x} y= {y} -> 1')
# elif x < 0 and y > 0:
#     print(f'х = {x} y= {y} -> 2')
# elif x < 0 and y < 0:
#     print(f'х = {x} y= {y} -> 3')
# elif x > 0 and y < 0:
#     print(f'х = {x} y= {y} -> 4')
# elif x == 0 and y != 0:
#     print('Точка пренадлежит оси Х')
# elif y == 0 and x != 0:
#     print('Точка пренадлежит оси Y')
# else:
#     print('Это координаты начала координат')


# 1. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

# num_quar = int(input('Введите номер четверти: '))
# if num_quar < 1 or num_quar > 4:
#     print('Четверти с таким номером не существует')
# elif num_quar == 1:
#     print('x > 0, y > 0')
# elif num_quar == 2:
#     print('x < 0, y > 0')
# elif num_quar == 3:
#     print('x < 0, y < 0')
# elif num_quar == 4:
#     print('x > 0, y < 0')

# 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math


# print('Введите координаты точки А, через запятую')
# A = [float(i) for i in input().split(',')]
# print('Введите координаты точки B, через запятую')
# B = [float(i) for i in input().split(',')]
# AB = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** (0.5)
# print(f'A({A[0]}, {A[1]}); B({B[0]}, {B[1]}) -> {math.floor(AB * 10 ** 2) / 10 ** 2}')
