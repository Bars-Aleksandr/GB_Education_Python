# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0, 56 -> 11


print('Введите число')
a = input()
sum = 0
lenght = len(a)
for i in range(lenght):
    if a[i] != ',' and a[i] != '.' and a[i] != ' ':
        sum = sum + int(a[i])
print(sum)
