"""
OK_ 1 Install PostgreSQL and PGAdmin4
OK_ 2 Create a database for 2 tables. One of them has a foreign key to another
ОК_ 3 Fill a few rows with test data in both of them
ОК_ 4 Create connection and cursor using psycopg2 in Python
ОК_ 5 Get data from one of these tables using cursor and psycopg2
6 Create a session with SQLAlchemy
7 Create dbModels classes for your tables, using Base = declarative_base() and inheritance
ОК_ 8 Create repositories for these tables with the next functional -
get_all(), get_item_by_id(), remove_item(), update_item(), add_item()"""

import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='hillel'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM opinions;")
result = cursor.fetchall()
print(result)

for opinion in result:
    print(opinion)

cursor.close()
connection.close()
