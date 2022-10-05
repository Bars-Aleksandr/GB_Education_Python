# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10 ^ {-1} ≤ d ≤10 ^ {-10}$

# def denominator(x): return x*(x+1)*(x+2)


# def num_pi(degree):
#     d = -degree
#     pi1 = 1
#     pi2 = 0
#     flag = 1
#     n = 2
#     while (pi1-pi2) >= 10**d:
#         if not flag % 2:
#             pi2 = pi1 - 4/denominator(n)
#         else:
#             pi1 = pi2 + 4/denominator(n)
#         flag += 1
#         n += 2
#     return 3+(pi1+pi2)/2


# degree = int(input('Enter the required precision: '))

# print('pi=', round(num_pi(degree), degree))
################################################################################################

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# def multiplier(n):
#     mult = []
#     count = 2
#     while n != 1:
#         if n % count == 0:
#             mult.append(count)
#             n /= count
#         elif n / count != 0:
#             count += 1
#     return mult


# n = int(input('Enter a natural number N: '))
# if len(multiplier(n)) != 1:
#     print(multiplier(n))
# else:
#     print(n, '-prime number')
#######################################################################################################

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def unique_list(entered_list):
    list = []
    for i in entered_list:
        if entered_list.count(i) == 1:
            list.append(i)
    return list


entered_list = list(map(int, input('Enter list: ').split()))
print(unique_list(entered_list))
########################################################################################################
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# from random import randint


# def get_elemements(k):
#     elements = [randint(0, 10) for i in range(k+1)]
#     return (elements)


# def get_polinom(k, elements):
#     elements_str = str(elements)
#     print(type(elements_str[0]))
#     # polinom = []
#     # var_x = []
#     for i in elements_str:
#         #     var_x.append('x^')
#         print(i, end='\n')
#     #     print(var_x)


# degree = int(input('Enter natural degree from 1 to 100: '))
# basic_elements = get_elemements(degree)
# get_polinom(degree, basic_elements)
# polynomial = ['2*x ^ 9', ' +', '10*x ^ 8', ' +', '8*x ^ 7', ' +', '4*x ^ 6', ' +',
#               '9*x ^ 5', ' +', '10*x ^ 4', ' +', '2*x ^ 3', ' +', '2*x2', ' +', '10', '= 0']
# # print('basic list', basic_elements)
# print("".join(map(str, polynomial)).replace(' 1*x', ' x'))
# from random import randint

# k = int(input('Insert equation power: '))
# koefs = list()
# for i in range(1, k + 2):
#     koefs.append(randint(1, 100))

# ans = list()
# for i in range(len(koefs)):
#     if k == 1:
#         ans.append(f'{koefs[i]}*x')
#     elif k == 0:
#         ans.append(f'{koefs[i]}')
#     else:
#         ans.append(f'{koefs[i]}*x**{k}')
#     flag = randint(0, 1)
#     if flag == 1:
#         ans.append('+')
#     elif flag == 0:
#         ans.append('-')
#     k -= 1

# ans.pop(-1)
# ans.append('=0')
# print(''.join(ans))
# fout = open('output.txt', 'w')
# fout.write(''.join(ans))
# fout.close()
