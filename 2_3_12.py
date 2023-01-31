# Задание
# Выведите список источников, из которых не было клиентов, либо клиенты пришедшие из которых не совершали заказов или
# отказывались от заказов. Под клиентами, которые отказывались от заказов, необходимо понимать клиентов, у которых есть
# заказы, которые на момент выполнения запроса находятся в состоянии 'rejected'. В запросе необходимо использовать
# оператор UNION для объединения выборок по разным условиям.

from mysql.connector import connect, Error

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='store'
) as connection:
    my_query = '''
        SELECT src.name FROM source as src
        LEFT OUTER JOIN client as clt ON clt.source_id = src.id WHERE clt.source_id IS NULL
        UNION
        SELECT src.name FROM source as src
        LEFT OUTER JOIN client as clt ON clt.source_id = src.id
        LEFT OUTER JOIN sale as sl ON sl.client_id = clt.id
        LEFT OUTER JOIN status as st ON st.id = sl.status_id WHERE st.name = 'rejected';
    '''
    with connection.cursor() as cursor:
        cursor.execute(my_query)
        res = cursor.fetchall()
        for row in res:
            print(row)