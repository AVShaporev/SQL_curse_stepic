from mysql.connector import connect, Error
import csv

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='yandex_practicum'
) as connection:
    with open(
            r'C:\Users\avsha\Documents\Curse_Yandex_Practicum_Python_Dev\01_Спринт\03_Введение в базы данных\[sharewood.biz] 04_CRUD создать, прочитать, обновить, удалить\products_data_all',
            encoding='utf8') as file:
        rows = csv.reader(file, delimiter=',')
        db_query = '''
        CREATE TABLE IF NOT EXISTS products_data_all (
            id_product INT PRIMARY KEY,
            name VARCHAR(255),
            category VARCHAR(255),
            units VARCHAR(255),
            weight INT,
            price DECIMAL(10,2),
            date_upd DATETIME,
            id_store INT,
            name_store VARCHAR(255)
            );
        '''
        with connection.cursor() as cursor:
            cursor.execute(db_query)
            connection.commit()

        try:
            for line in list(rows)[1:]:
                db_query = f"INSERT INTO products_data_all (id_product, name, category, units, weight, price, date_upd, id_store, name_store) VALUES({int(line[0])}, '{line[1]}', '{line[2]}', '{line[3]}', '{0 if line[4] == 'NULL' else int(line[4])}', '{line[5]}', '{line[6]}', '{int(line[7])}', '{line[8]}');"
                with connection.cursor() as cursor:
                    cursor.execute(db_query)
                    connection.commit()
        except Error as er:
            print(line)
            print(er)