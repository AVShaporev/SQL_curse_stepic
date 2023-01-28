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
    INSERT INTO billing (
        payer_email, recipient_email,
        sum, currency, billing_date)
    VALUES (
    'alex@mail.com',
    'leo@mail.com',
    '500.00', 'MYR',
    '2010-08-20');
    '''
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        connection.commit()