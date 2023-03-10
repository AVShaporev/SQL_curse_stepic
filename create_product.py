from mysql.connector import connect, Error
import csv

base = 'products_data_all'
path = 'C:\\Users\\avsha\\Documents\\Curse_Yandex_Practicum_Python_Dev\\01_Спринт\\03_Введение в базы данных\[sharewood.biz] 04_CRUD создать, прочитать, обновить, удалить\\'

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='yandex_practicum'
) as connection:
    with open(path + base,
              encoding='utf8') as file:
        rows = csv.reader(file, delimiter=',')
        db_query = '''
        CREATE TABLE IF NOT EXISTS products_data_all (
            id_product INT,
            name VARCHAR(255),
            category VARCHAR(50),
            units VARCHAR(10),
            weight DECIMAL (10,2),
            price DECIMAL(10,2),
            date_upd DATETIME,
            id_store INT,
            name_store VARCHAR(50)
            );
        '''
        with connection.cursor() as cursor:
            cursor.execute(db_query)
            connection.commit()

        try:
            for line in list(rows)[1:]:
                print(line)
                db_query = f"INSERT INTO {base}(id_product, name, category, units, weight, price, date_upd, id_store, name_store) VALUES('{int(line[0])}', '{line[1]}', '{line[2]}', '{line[3]}', '{0 if line[4] == 'NULL' else float(line[4])}', '{0 if line[5] == 'NULL' else float(line[5])}', '{line[6]}', '{int(line[7])}', '{line[8]}');"
                with connection.cursor() as cursor:
                    cursor.execute(db_query)
                    connection.commit()
                print('Запись добавлена')
        except Error as er:
            print(line)
            print(er)