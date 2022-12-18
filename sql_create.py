import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")
    cursor = connection.cursor()
    # СОЗДАЕМ ТАБЛИЦУ
    create_table_query = '''CREATE TABLE notes
                          (ID INT PRIMARY KEY     NOT NULL,
                          USER           TEXT    NOT NULL,
                          NOTE         TEXT); '''
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица  создана")

except (Exception, Error) as error:
    print("Ошибка", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")
