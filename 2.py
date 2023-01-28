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
    db_query = '''
    UPDATE billing
        SET payer_email='igor@mail.com'
    WHERE payer_email='alex@mail.com';
    '''
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        connection.commit()