import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres_db")

    cursor = connection.cursor()
    # Написан SQL-запрос для добавления пользователя
    insert_query = """ INSERT INTO notes (ID, USER) VALUES (2, 'Egor')"""
    #Написан SQL-запрос для добавления объявления
    insert_query = """ INSERT INTO notes (ID, USER, DATA) VALUES (2, 'Egor', 'ЭТО МОЯ ЗАПИСЬ!')"""
    cursor.execute(insert_query)
    connection.commit()
    print("Запись добавлена")
    # Написан SQL-запрос для вывода списка объявлений с данными пользователей, их создавших
    cursor.execute("SELECT user, data from notes")
    record = cursor.fetchall()
    print("Результат", record)

    # писан SQL-запрос для удаления объявления
    delete_query = """delete from notes where id = 2"""
    cursor.execute(delete_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "Запись удалена")
    cursor.execute("SELECT * from notes")
    print("Результат", cursor.fetchall())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")
