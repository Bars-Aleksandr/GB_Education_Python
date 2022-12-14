# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math


print('Введите координаты точки А, через запятую')
A = [float(i) for i in input().split(',')]
print('Введите координаты точки B, через запятую')
B = [float(i) for i in input().split(',')]
AB = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** (0.5)
print(f'A({A[0]}, {A[1]}); B({B[0]}, {B[1]}) -> {math.floor(AB * 10 ** 2) / 10 ** 2}')
