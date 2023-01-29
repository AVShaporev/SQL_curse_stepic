from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='project_simple'
) as connection:
    create_db_query = '''    
    SELECT
        AVG(DATEDIFF(project_finish, project_start)) as avg_days,
        MAX(DATEDIFF(project_finish, project_start)) as max_days,
        MIN(DATEDIFF(project_finish, project_start)) as min_days,
        client_name
    FROM project WHERE project_finish IS NOT NULL
    GROUP BY client_name
    ORDER BY max_days DESC
    LIMIT 10;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)