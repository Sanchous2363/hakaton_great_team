import sqlite3

def prepare_database_for_weather():
    connection = sqlite3.connect('users.db')
    cur = connection.cursor()

    query = (f'CREATE TABLE IF NOT EXISTS users' \
                    f'(id INTEGER AUTO_INCREMENT PRIMARY KEY, ' \
                    f'user_id INTEGER, ' \
                    f'city TEXT, ' \
                    f'description TEXT, ' \
                    f'humidity INTEGER,' \
                    f'temp INTEGER)')

    cur.execute(query)
    connection.commit()
    cur.close()

def add_all(id, city, description, humidity,temp):
    connection = sqlite3.connect('users.db')
    cur = connection.cursor()
    first_info = (id, city, description, humidity, temp)
    cur.execute(
        f'INSERT INTO users (user_id, city, description, humiditi, temp) VALUES (?, ?, ?, ?, ?);',
        first_info)
    connection.commit()
    cur.close()

def get_city(id):
    connection = sqlite3.connect('users.db')
    cur = connection.cursor()
    results = cur.execute(
        f'SELECT city FROM users WHERE user_id = {id} ORDER BY id DESC;')
    for i in results:
        return str(i[0])
    connection.commit()
    cur.close()

def get_all_weather(id):
    connection = sqlite3.connect('users.db')
    cur = connection.cursor()
    results = cur.execute(
        f'SELECT description, humidity,temp FROM users WHERE user_id = {id} ORDER BY id DESC;')
    for i in results:
        all_weather = str(i[0]) + str(i[1]) + str(i[2])
        return all_weather
    connection.commit()
    cur.close()
