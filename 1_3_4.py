# аза данных учета проектов `project_simple` состоит из одной таблицы `project` следующей структуры:
#
#
#
# CREATE TABLE IF NOT EXISTS `project_simple`.`project` (
#   `project_name` VARCHAR(255) NULL,
#   `client_name` VARCHAR(255) NULL,
#   `project_start` DATE NULL,
#   `project_finish` DATE NULL,
#   `budget` DECIMAL(18,2) NULL)
# ENGINE = InnoDB;
#
# Задание
# Выведите общее количество заказов компании.


from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='store_simple'
) as connection:
    create_db_query = '''    
    SELECT
        COUNT(1)
    FROM store;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)