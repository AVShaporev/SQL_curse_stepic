from mysql.connector import connect, Error

with connect(
    host='localhost',
    user='root',
    password='12345',
    database='project_simple'
) as connection:
    create_db_query = '''
    SELECT AVG(budget) FROM project;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)