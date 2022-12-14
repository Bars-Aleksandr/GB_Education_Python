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


# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№ Рекурсия  №№№№№№№№№№№№№№№№№№
# def fib(n):
#  if n in [1, 2]:
#  return 1             НЕЗАБЫВАЕМ ОБ УСЛОВИИ ПРИ КОТОРОМ НАДО ВЫЙТИ ИЗ ФУНКЦИИ
#  else:
#  return fib(n-1) + fib(n-2)


# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list)  # 1 1 2 3 5 8 13 21 34


############################################ Кортежи - неизменяемый список #################
# t = ()
# print(type(t))  # tuple
# t = (1,)
# print(type(t))  # tuple
# t = (1)
# print(type(t))  # int
# t = (28, 9, 1990)
# print(type(t))  # tuple
# colors = ['red', 'green', 'blue']
# print(colors)  # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t)  # ('red', 'green', 'blue')


# # t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue


########################### Словари Неупорядоченные коллекции произвольных объектов с доступом по ключу #####

# dictionary = {}  создали пустой словарь
# dictionary = \   создали словарь с доступом по ключу \ - чтобы значения писались с новой строки
#     {
#         'up': '↑',     'up' - ключ что справо это значение
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)  # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])  # ←

# for k in dictionary.keys:
#     print(k)                  можно посмотреть все ключи

# for k in dictionary.values:
#     print(k)                  можно посмотреть все значения

# # типы ключей могут отличаться

# print(dictionary['up'])  # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left'])  # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left']  # удаление элемента
# for item in dictionary:  # for (k,v) in dictionary.items(): ПОЛУЧЕНИЕ СЛОВАРЯ ПАРАМИ
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →


############################### Множества -неупорядоченная совокупность элементов ЭТО ТИП ДАННЫХ ################

a = {1, 2, 3, 5, 8}
b = {'2', '5', 8, 13, 21}
print(type(a))  # set
print(type(b))  # set

###########################
a = {1, 2, 3, 5, 8}
b = set([2, 5, 8, 13, 21])
c = set((2, 5, 8, 13, 21))
print(type(a))  # set
print(type(b))  # set
print(type(c))  # set
a = {1, 1, 1, 1, 1}
print(a)  # {1}

############################
colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')
print(colors)  # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
colors.discard('red')  # ok
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { }
print(colors)  # set()

######################################
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8}
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)  # i = {8, 2, 5}
dl = a.difference(b)  # dl = {1, 3}
dr = b.difference(a)  # dr = {13, 21}
q = a \
    .union(b) \
    .difference(a.intersection(b))
# {1, 21, 3, 13}

####################################
################################## Неизменяемое множество ################
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8})
