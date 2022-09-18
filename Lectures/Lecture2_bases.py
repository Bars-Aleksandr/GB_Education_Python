# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# # data - это переменная, к data привязать file.txt с атрибутом 'w' в этом случае data.close() не обязательно
# with open('file.txt', 'w') as data:
#     # записать в файл строку line 1 и /n сделается переход на другую строку
#     data.write('line 1\n')
#     data.write('line 2\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)  # разделителей не будет
# data.close()

# path = 'file.txt'  # присвоить к файлой переменной файл
# data = open(path, 'r')  # открыть файл для чтения
# for line in data:
#     print(line)  # считаные строки вывести в консоль
# data.close()  # закрыть файл

# Функции
# Это фрагмент программы, используемый
# многократно


# def function_name(x):
#     # body line 1
#     # . . .
#     # body line n
#  # optional return

# Использование функций из файла function-file и присвоить псевдоним к файлу ff
# import function_file as ff
# import function_file


# def f(x):
#     return x**2


# def f(x):
#     if x == 1:
#     return 'Целое'
#     elif x == 2.3:
#     return 23
#     else:
#     return


# print(f(1))  # Целое
# print(f(2.3))  # 23
# print(f(28))  # None
# print(type(f(1)))  # str
# print(type(f(2.3)))  # int
# print(type(f(28)))  # NoneType


# # new file function_file.py
# #############################

# def f(x):
#     if x == 1:
#     return 'Целое'
#     elif x == 2.3:
#     return 23
#     else:
#     return


# file hello.py
# print(function_file.f(1))  # Целое
# print(function_file.f(2.3))  # 23
# print(function_file.f(28))  # None

# # 333
# # new file function_file.py


# def f(x):
#     if x == 1:
#     return 'Целое'
#     elif x == 2.3:
#     return 23
#     else:
#     return


# file hello.py
# print(ff.f(1))  # Целое
# print(ff.f(2.3))  # 23
# print(ff.f(28))  # None

# ##################################


# def new_string(symbol, count):
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # TypeError missing 1 required ...


# #####################################
# def new_string(symbol, count=3):
#     return symbol * count


# print(new_string('!', 5))  # !!!!!
# print(new_string('!'))  # !!!
# print(new_string(4))  # 12
# # при передаче автоматически произошло преобразование типа


# ######################################
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#     res += item
#     return res


# print(concatenatio('a', 's', 'd', 'w'))  # asdw
# print(concatenatio('a', '1', 'd', '2'))  # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ...
