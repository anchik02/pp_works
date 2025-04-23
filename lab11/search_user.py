import psycopg2

def search_contacts():
    pattern = input("Введите шаблон (часть имени или номера): ").strip()
    
    if not pattern:
        print("Ошибка: пустой ввод")
        return

    try:
        # Connect to database
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        
        with conn.cursor() as cur:
            # Use direct SQL query instead of function
            cur.execute("""
                SELECT id, name, phone 
                FROM phonebook
                WHERE name ILIKE %s OR phone LIKE %s
                ORDER BY name
            """, (f'%{pattern}%', f'%{pattern}%'))
            
            rows = cur.fetchall()
            
            if not rows:
                print("Записи не найдены")
            else:
                print("\nРезультаты поиска:")
                print("{:<5} {:<20} {:<15}".format("ID", "Имя", "Телефон"))
                print("-" * 40)
                for row in rows:
                    print("{:<5} {:<20} {:<15}".format(row[0], row[1], row[2]))
                    
    except psycopg2.Error as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    search_contacts()