import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="postgres",  
        user="postgres",     
        password="postgres",  
        host="localhost"       
    )

def read_all_rows():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM employees") 
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Ошибка при чтении всех строк: {e}")
    finally:
        cursor.close()
        conn.close()

def read_one_row(row_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM employees WHERE id = %s", (row_id,))
        row = cursor.fetchone()
        if row:
            print(row)
        else:
            print(f"Запись с id {row_id} не найдена.")
    except Exception as e:
        print(f"Ошибка при чтении одной строки: {e}")
    finally:
        cursor.close()
        conn.close()

def perform_crud_operations():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO employees (name, position) VALUES (%s, %s)", ('John Doe', 'Developer'))
        
        cursor.execute("SELECT * FROM employees WHERE name = %s", ('John Doe',))
        row = cursor.fetchone()
        print("Чтение: ", row)

        cursor.execute("UPDATE employees SET position = %s WHERE name = %s", ('Senior Developer', 'John Doe'))
        
        cursor.execute("DELETE FROM employees WHERE name = %s", ('John Doe',))

        conn.commit()
        print("Операции успешно выполнены.")
    except Exception as e:
        conn.rollback()
        print(f"Ошибка в операции CRUD: {e}")
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    print("Чтение всех строк:")
    read_all_rows()
    
    print("\nЧтение одной строки:")
    read_one_row(1)  

    print("\nВыполнение операций CRUD:")
    perform_crud_operations()
