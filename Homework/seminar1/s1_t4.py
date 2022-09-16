# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

num_quar = int(input('Введите номер четверти: '))
if num_quar < 1 or num_quar > 4:
    print('Четверти с таким номером не существует')
elif num_quar == 1:
    print('x > 0, y > 0')
elif num_quar == 2:
    print('x < 0, y > 0')
elif num_quar == 3:
    print('x < 0, y < 0')
elif num_quar == 4:
    print('x > 0, y < 0')
