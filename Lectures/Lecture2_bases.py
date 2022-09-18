# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# data - это переменная, к data привязать file.txt с атрибутом 'w' в этом случае data.close() не обязательно
with open('file.txt', 'w') as data:
    # записать в файл строку line 1 и /n сделается переход на другую строку
    data.write('line 1\n')
    data.write('line 2\n')

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)  # разделителей не будет
data.close()

path = 'file.txt'  # присвоить к файлой переменной файл
data = open(path, 'r')  # открыть файл для чтения
for line in data:
    print(line)  # считаные строки вывести в консоль
data.close()  # закрыть файл
