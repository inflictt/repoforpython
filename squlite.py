# import sqlite3
# conn= sqlite3.connect("to_do_list_.db")
# conn.execute('''
#             Create table tasks(
#                 task STR AUTO_INCREMENT PRIMARY KEY
#                 date INT  
#             )
#              ''')
# conn.close
import sqlite3

conn = sqlite3.connect("to_do_list.db")  # Correct the database name
conn.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        date TEXT NOT NULL
    )
''')
conn.close()
