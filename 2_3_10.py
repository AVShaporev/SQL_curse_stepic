# Задание
# Выведите названия товаров, которые относятся к категории 'Cakes' или фигурируют в заказах текущий статус которых
# 'delivering'. Результат не должен содержать одинаковых записей. В запросе необходимо использовать оператор UNION для
# объединения выборок по разным условиям.

from mysql.connector import connect, Error

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='store'
) as connection:
    my_query = '''

    '''
    with connection.cursor() as cursor:
        cursor.execute(my_query)
        res = cursor.fetchall()
        for row in res:
            print(row)