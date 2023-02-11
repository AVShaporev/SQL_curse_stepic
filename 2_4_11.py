from mysql.connector import connect, Error

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='yandex_practicum'
) as connection:
    with open(r'C:\Users\avsha\Documents\Curse_Yandex_Practicum_Python_Dev\01_Спринт\03_Введение в базы данных\[sharewood.biz] 04_CRUD создать, прочитать, обновить, удалить',
              'r') as file:
        for line in file.readlines():

        my_query = '''
            CRE
        '''
        with connection.cursor() as cursor:
            cursor.execute(my_query)
            res = cursor.fetchall()
            for row in res:
                print(row)