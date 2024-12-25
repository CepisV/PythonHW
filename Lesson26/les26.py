import psycopg2

try:
    conn = psycopg2.connect(
        dbname = 'step',
        user = 'postgres',
        password = 'postgres',
        host = 'localhost',
        port='5432'
    )
    print('connection established')
except Exception as e:
    print(f'Error {e}')