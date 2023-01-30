# Задание
# Выведите список товаров с названиями категорий, в том числе товаров, не принадлежащих ни к одной из категорий, в том
# числе категорий не содержащих ни одного товара.
# Ожидаемый формат результата:

from mysql.connector import connect, Error

with connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='store'
) as connection:
    my_query = '''
        SELECT good.name AS good_name, category.name AS category_name FROM good
            LEFT OUTER JOIN category_has_good
                ON category_has_good.good_id = good.id
            LEFT OUTER JOIN category
                ON category_has_good.category_id = category.id
            UNION
            SELECT good.name AS good_name, category.name AS category_name FROM good
            RIGHT OUTER JOIN category_has_good
                ON category_has_good.good_id = good.id
            RIGHT OUTER JOIN category
                ON category_has_good.category_id = category.id
            ORDER BY good_name, category_name;
    '''
    with connection.cursor() as cursor:
        cursor.execute(my_query)
        res = cursor.fetchall()
        for row in res:
            print(row)