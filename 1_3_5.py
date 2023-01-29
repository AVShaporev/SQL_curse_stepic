# Исходные данные
# База данных магазина `store_simple` состоит из одной таблицы `store` следующей структуры:
#
#
#
# CREATE TABLE IF NOT EXISTS `store_simple`.`store` (
#   `product_name` VARCHAR(255) NULL,
#   `category` VARCHAR(255) NULL,
#   `price` DECIMAL(18,2) NULL,
#   `sold_num` INT NULL)
# ENGINE = InnoDB;
#
# Задание
# Выведите количество товаров в каждой категории. Результат должен содержать два столбца:
# название категории,
# количество товаров в данной категории.

from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='store_simple'
) as connection:
    create_db_query = '''    
    SELECT
        category, COUNT(1)
    FROM store
    GROUP BY category;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)