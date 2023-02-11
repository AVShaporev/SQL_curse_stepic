from mysql.connector import connect, Error
import csv

base = 'transactions'
path = 'C:\\Users\\avsha\\Documents\\Curse_Yandex_Practicum_Python_Dev\\01_Спринт\\03_Введение в базы данных\[sharewood.biz] 04_CRUD создать, прочитать, обновить, удалить\\'

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='yandex_practicum'
) as connection:

    db_query = '''
    CREATE TABLE IF NOT EXISTS transactions (
        user_id INT,
        id_transaction INT,
        id_store INT,
        id_product INT,
        date DATETIME,
        unique_id INT PRIMARY KEY
        );
    '''

    with connection.cursor() as cursor:
        cursor.execute(db_query)
        connection.commit()

    with open(path + base,
              encoding='utf8') as file:
        rows = csv.reader(file, delimiter=',')

        try:
            for line in list(rows)[1:]:
                print(line)
                db_query = f"INSERT INTO {base}(user_id, id_transaction, id_store, id_product, date, unique_id) VALUES('{int(line[0])}', '{int(line[1])}', '{int(line[2])}', '{int(line[3])}', '{line[4]}', '{int(line[5])}');"
                with connection.cursor() as cursor:
                    cursor.execute(db_query)
                    connection.commit()
                print('Запись добавлена')
        except Error as er:
            print(line)
            print(er)