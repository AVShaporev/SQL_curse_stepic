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
    GROUP BY category
    ORDER BY category;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)