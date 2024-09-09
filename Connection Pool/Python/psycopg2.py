import psycopg2
from psycopg2 import pool

connection_pool = psycopg2.pool.SimpleConnectionPool(
    1,  # minimum number of connections
    20,  # maximum number of connections
    user='postgres',
    password='changeme',
    host='127.0.0.1',
    port='5432',
    database='connect_pool'
)

connection = connection_pool.getconn()

cursor = connection.cursor()
cursor.execute('SELECT * FROM users')
result = cursor.fetchall()

print(result)

connection_pool.putconn(connection)

