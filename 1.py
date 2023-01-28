from getpass import getpass
from mysql.connector import connect, Error
# import mysql

# try:
with connect(
    host='localhost',
    user='root',
    password='12345',
    database='billing_simple'
) as connection:
    create_db_query = '''
    SELECT * FROM billing 
    WHERE payer_email IS NULL
    OR recipient_email IS NULL;
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
        res = cursor.fetchall()
        for row in res:
            print(row)
# except Error as e:
#     print(e)


# cnx.sel
# cnx = MySQLConnection(user='joe', database='test')

# try:
#     with connect(
#         host="localhost",
#         user=input("Имя пользователя: "),
#         password=getpass("Пароль: "),
#         database='billing_simple',
#     ) as connection:
#         print(connection)
# except Error as e:
#     print(e)