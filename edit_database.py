import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect('sqlite.db', check_same_thread=False)
cursor = connection.cursor()
cursor.execute('DROP TABLE user')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS user 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, 
        username TEXT UNIQUE NOT NULL, 
        password_hash TEXT NOT NULL);
            ''')

# cursor.execute('ALTER TABLE post ADD author_id INTEGER;')
cursor.execute('INSERT INTO user VALUES (?, ?, ?)',(1, 'Rocket', generate_password_hash('52389562895639563568936349867897354682986')))
cursor.execute('UPDATE post SET author_id= 1;')


connection.commit()
connection.close()

