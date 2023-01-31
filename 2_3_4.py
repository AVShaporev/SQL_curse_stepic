# Задание
# Выведите все позиций списка товаров принадлежащие какой-либо категории с названиями товаров и названиями категорий.
# Список должен быть отсортирован по названию товара, названию категории. Для соединения таблиц необходимо использовать
# оператор INNER JOIN.

from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='STORE'
) as connection:
    create_db_query = '''    
        SELECT good.name AS good_name, category.name AS cat_name FROM good
            INNER JOIN category_has_good
                ON category_has_good.good_id = good.id
            INNER JOIN category
                ON category_has_good.category_id = category.id
            ORDER BY good_name, cat_name;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)