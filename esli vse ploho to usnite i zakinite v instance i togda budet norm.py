import sqlite3


def create_bd():  # создаем подключение к базе данных
    conn = sqlite3.connect('notes.db')

    # создаем курсор
    cursor = conn.cursor()

    # создаем таблицу для хранения заметок
    cursor.execute('''CREATE TABLE IF NOT EXISTS note
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT,
                   content TEXT,
                   theme TEXT)''')

    # сохраняем изменения
    conn.commit()

    # закрываем соединение
    conn.close()
