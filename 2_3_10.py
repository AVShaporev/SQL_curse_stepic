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
        SELECT good.name as good_name FROM good
            INNER JOIN category_has_good as chd
                ON chd.good_id = good.id
            INNER JOIN category as cat
                ON cat.id = chd.category_id
                AND cat.name = 'Cakes'
        UNION
        SELECT good.name as good_name FROM good
            INNER JOIN sale_has_good as shd
                ON shd.good_id = good.id
            INNER JOIN sale
                ON sale.id = shd.sale_id
            INNER JOIN status
                ON status.id = sale.status_id
                AND status.name = 'delivering';
    '''
    with connection.cursor() as cursor:
        cursor.execute(my_query)
        res = cursor.fetchall()
        for row in res:
            print(row)