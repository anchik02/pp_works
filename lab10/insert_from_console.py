import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

name = input("Enter name: ")
phone = input("Enter phone: ")

cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))

conn.commit()
cur.close()
conn.close()
print("Data inserted successfully.")