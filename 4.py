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
    INSERT INTO billing 
    VALUES (
    'pasha@mail.com',
    'katya@mail.com',
    '300.00', 'EUR',
    '2016-02-14',
    'Valentines day present');
    '''
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        connection.commit()