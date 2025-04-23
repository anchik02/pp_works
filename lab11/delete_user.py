import psycopg2

def delete_user():
    query = input("Введите имя или номер для удаления: ").strip()
    
    if not query:
        print("Ошибка: пустой ввод")
        return

    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        
        with conn.cursor() as cur:
            # First try to delete by phone
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (query,))
            deleted_count = cur.rowcount
            
            # If nothing deleted, try by name
            if deleted_count == 0:
                cur.execute("DELETE FROM phonebook WHERE name = %s", (query,))
                deleted_count = cur.rowcount
            
            conn.commit()
            
            if deleted_count > 0:
                print(f"Удалено записей: {deleted_count}")
            else:
                print("Записи с таким именем или номером не найдены")
                
    except psycopg2.Error as e:
        print(f"Ошибка базы данных: {e}")
        if 'conn' in locals():
            conn.rollback()
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    delete_user()