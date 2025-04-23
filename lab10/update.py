import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

print("1. Update name by phone")
print("2. Update phone by name")
choice = input("Choose option (1 or 2): ")

if choice == "1":
    phone = input("Enter phone number to update name: ")
    new_name = input("Enter new name: ")
    cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
elif choice == "2":
    name = input("Enter name to update phone: ")
    new_phone = input("Enter new phone: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
else:
    print("Invalid option.")

conn.commit()
cur.close()
conn.close()
print("Update complete.")