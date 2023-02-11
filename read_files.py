import csv

file = 'products_stores'
path = 'C:\\Users\\avsha\\Documents\\Curse_Yandex_Practicum_Python_Dev\\01_Спринт\\03_Введение в базы данных\[sharewood.biz] 04_CRUD создать, прочитать, обновить, удалить\\'
with open(path + file,
          encoding='utf8') as file:
    rows = csv.reader(file, delimiter=',')
    for num, line in enumerate(list(rows)[:]):
        print(num, line)