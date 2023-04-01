import sqlite3

conn = sqlite3.connect('kwamina.db')
c = conn.cursor()

# Create the user table
c.execute('''CREATE TABLE user
             (id INT PRIMARY KEY, username TEXT)''')

# Create the user_interaction table with foreign key
c.execute('''CREATE TABLE user_interaction
             (id INT PRIMARY KEY, user_id INT, user_messages TEXT, response TEXT,
              FOREIGN KEY(user_id) REFERENCES user(id))''')

conn.commit()
conn.close()