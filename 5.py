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
    DELETE FROM billing
    WHERE payer_email is NULL OR payer_email=''
    OR recipient_email is NULL OR recipient_email='';
    '''
    with connection.cursor() as cursor:
        cursor.execute(db_query)
        connection.commit()