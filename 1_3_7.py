# Исходные данные
# База данных учета проектов `project_simple` состоит из одной таблицы `project` следующей структуры:
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
# Выведите в качестве результата одного запроса общее количество заказов, сумму стоимостей (бюджетов) всех проектов, средний срок исполнения заказа в днях.
#
# NB! Для вычисления длительности проекта удобно использовать встроенную функцию datediff().

from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='project_simple'
) as connection:
    create_db_query = '''    
    SELECT
        COUNT(1) as kol,
        SUM(budget) as sym,
        AVG(DATEDIFF(project_finish, project_start)) as dif_days
    FROM project;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)