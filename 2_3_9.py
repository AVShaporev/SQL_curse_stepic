# Задание
# Выведите список всех источников клиентов и суммарный объем заказов по каждому источнику. Результат должен включать
# также записи для источников, по которым не было заказов.
# Ожидаемый формат результата:

from mysql.connector import connect, Error

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='store'
) as connection:
    my_query = '''
        SELECT s.name AS source_name, sum(sh.sale_sum) as sale_sum FROM source as s
            LEFT JOIN client  as cl
                ON s.id = cl.source_id
            LEFT JOIN sale as sh
                ON sh.client_id = cl.id
                GROUP BY source_name;
    '''
    with connection.cursor() as cursor:
        cursor.execute(my_query)
        res = cursor.fetchall()
        for row in res:
            print(row)