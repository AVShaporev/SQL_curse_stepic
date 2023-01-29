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
# Выведите 5 категорий товаров, продажи которых принесли наибольшую выручку. Под выручкой понимается сумма произведений
# стоимости товара на количество проданных единиц. Результат должен содержать два столбца:
# название категории,
# выручка от продажи товаров в данной категории.

from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='store_simple'
) as connection:
    create_db_query = '''    
    SELECT
        category, sum(sold_num * price) as vyr
    FROM store
    GROUP BY category
    ORDER BY vyr DESC
    LIMIT 5;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)