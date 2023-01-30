# Задание
# Выведите список товаров с названиями товаров и названиями категорий, в том числе товаров, не принадлежащих ни одной из
# категорий.

from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='store'
) as connection:
    create_db_query = '''    
        SELECT good.name AS good_name, category.name AS category_name FROM good
            LEFT OUTER JOIN category_has_good
                ON category_has_good.good_id = good.id
            LEFT OUTER JOIN category
                ON category_has_good.category_id = category.id
            ORDER BY good_name, category_name;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)