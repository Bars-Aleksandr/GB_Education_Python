# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли
# этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
print('Введите день недели цифрой')
weekend = int(input())
if weekend in [6, 7]:
    print(weekend, '->', 'да')
else:
    print(weekend, '->', 'нет')
