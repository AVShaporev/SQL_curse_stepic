# Задание
# Выведите список всех категорий продуктов и количество продаж товаров, относящихся к данной категории. Под количеством
# продаж товаров подразумевается суммарное количество единиц товара данной категории, фигурирующих в заказах с любым
# статусом.

from mysql.connector import connect, Error

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='store'
) as connection:
    my_query = '''
        SELECT c.name, COUNT(sale.id) as sale_num FROM category as c
            LEFT OUTER JOIN category_has_good as chg ON chg.category_id = c.id
                LEFT OUTER JOIN good ON good.id = chg.good_id
                    LEFT OUTER JOIN sale_has_good as shg ON shg.good_id = good.id
                        LEFT OUTER JOIN sale ON sale.id = shg.sale_id
                        GROUP BY c.name;
    '''
    with connection.cursor() as cursor:
        cursor.execute(my_query)
        res = cursor.fetchall()
        for row in res:
            print(row)