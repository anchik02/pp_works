import psycopg2
import re

def validate_phone(phone):
    """Check if phone has 10-20 digits"""
    return re.match(r'^\d{10,20}$', phone) is not None

def main():
    # Get user input
    names_input = input("Введите имена через запятую: ")
    phones_input = input("Введите номера через запятую: ")
    
    names = [name.strip() for name in names_input.split(",") if name.strip()]
    phones = [phone.strip() for phone in phones_input.split(",") if phone.strip()]

    # Validate input
    if len(names) != len(phones):
        print("Ошибка: количество имен и номеров не совпадает.")
        return

    invalid_records = []
    success_count = 0
    
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
            # Process each record
            for name, phone in zip(names, phones):
                if not validate_phone(phone):
                    invalid_records.append(f"Неверный формат телефона: {phone} для {name}")
                    continue
                
                try:
                    # First try to insert
                    cur.execute(
                        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                        (name, phone)
                    )
                    success_count += 1
                except psycopg2.IntegrityError:
                    # If phone exists, update the name
                    try:
                        cur.execute(
                            "UPDATE phonebook SET name = %s WHERE phone = %s",
                            (name, phone)
                        )
                        success_count += 1
                    except psycopg2.Error as e:
                        invalid_records.append(f"Ошибка обновления: {e} - Имя: {name}, Телефон: {phone}")
                except psycopg2.Error as e:
                    invalid_records.append(f"Ошибка вставки: {e} - Имя: {name}, Телефон: {phone}")
            
            conn.commit()
            
            # Show results
            print(f"\nУспешно обработано записей: {success_count}")
            if invalid_records:
                print("Некорректные записи:")
                for record in invalid_records:
                    print(f" - {record}")
            
    except psycopg2.Error as e:
        print(f"Ошибка базы данных: {e}")
        if 'conn' in locals():
            conn.rollback()
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    main()