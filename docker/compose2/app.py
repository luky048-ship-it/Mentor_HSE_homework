import os



print("Hello from Docker!")
print("DB Host from env:", os.getenv("DB_HOST", "default"))


try:
    from psycopg2 import connect
    conn = connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 5432)),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "secret"),
            dbname=os.getenv("DB_NAME", "app_db")
            )
    print("Подключение к Postgres успешно! Hello from DB!")
    conn.close()
exept Exception as e:
    print("Ошибка подключения (db может не быть готова):", e)
