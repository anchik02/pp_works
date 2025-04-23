import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

print("1. Delete by name")
print("2. Delete by phone")
choice = input("Choose option (1 or 2): ")

if choice == "1":
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
elif choice == "2":
    phone = input("Enter phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
else:
    print("Invalid choice.")

conn.commit()
cur.close()
conn.close()
print("Delete complete.")