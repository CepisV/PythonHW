import psycopg2

def connect_to_db():
    return psycopg2.connect(
        dbname="step",
        user="postgrese",
        password="postgrese",
        host="localhost",
        port="5432"
    )

def read_all_rows():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM example_table;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_one_row(row_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM example_table WHERE id = %s;", (row_id,))
    row = cursor.fetchone()
    cursor.close()
    connection.close()
    return row

def insert_row(data):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO example_table (column1, column2) VALUES (%s, %s);", 
        data
    )
    connection.commit()
    cursor.close()
    connection.close()

def delete_row(row_id):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM example_table WHERE id = %s;", (row_id,))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    insert_row(("value1", "value2"))
    
    print("All rows:", read_all_rows())
    
    print("Single row:", read_one_row(1))
    
    delete_row(1)
    print("After deletion:", read_all_rows())
