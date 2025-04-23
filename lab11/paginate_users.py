import psycopg2

limit = int(input("Сколько записей показать? "))
offset = int(input("Сколько пропустить? "))

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432")
cur = conn.cursor()

cur.execute("SELECT * FROM get_users_paginated(%s, %s);", (limit, offset))
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()