from readline import insert_text
from venv import create

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor()as cursor:
        create_query = """
        CREATE TABLE IF NOT EXISTS employee(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """

        cursor.execute(create_query)

        insert_query ='INSERT INTO employee(name,department) VALUES(%s,%s)'
        value=[('jhon','it'),('alice','hr'),('bob','finance')]
        cursor.executemany(insert_query,value)
        connection.commit()

        select_query='SELECT * FROM employee'
        cursor.execute(select_query)
        result=cursor.fetchall()

        for row in result:
            print(row)

finally:
    connection.close()