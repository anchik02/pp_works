import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

print("1. Show all records")
print("2. Search by name")
print("3. Search by phone")
choice = input("Choose option (1/2/3): ")

if choice == "1":
    cur.execute("SELECT * FROM phonebook")
elif choice == "2":
    name = input("Enter name to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + name + '%',))
elif choice == "3":
    phone = input("Enter phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", ('%' + phone + '%',))
else:
    print("Invalid choice.")

rows = cur.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

cur.close()
conn.close()