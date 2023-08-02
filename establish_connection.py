

import psycopg2
def establish_connection():
    conn = psycopg2.connect(
        database='studentinfo',
        user='postgres',
        password='666988',
        host='127.0.0.1',
        port=5432
    )

    conn.autocommit = True
    print("Connection established successfully !!")
    cursor = conn.cursor()
    return cursor
