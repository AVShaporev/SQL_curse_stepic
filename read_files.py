import csv

with open(r'C:\Users\avsha\Documents\Curse_Yandex_Practicum_Python_Dev\01_Спринт\03_Введение в базы данных\[sharewood.biz] 04_CRUD создать, прочитать, обновить, удалить\products_data_all',
          encoding='utf8') as file:
    rows = csv.reader(file, delimiter=',')
    for line in list(rows)[6:10]:
        print(line)