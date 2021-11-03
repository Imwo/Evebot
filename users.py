import sqlite3
conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
    ID INT,
    firstname TEXT,
    surname TEXT,
    age INT,
    class INT
    );
""")
conn.commit()
