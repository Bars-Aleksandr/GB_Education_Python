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
        if i not in list:
            list.append(i)
    return list


entered_list = list(map(int, input('Enter list: ').split()))
print(unique_list(entered_list))
