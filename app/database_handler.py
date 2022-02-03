import sqlite3 as sql
import collection_handler

class edit_db():
    def __init__(self):
        self.database = sql.connect('collections.db')
        self.cursor = self.database.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS database (Collection, Apps)''')

    def create_collection(self):
        self.cursor.execute(f'''INSERT INTO database VALUES ('{collection_handler.collection_repo[0]}', '{collection_handler.collection_repo[1]}')''')
        self.database.commit()



dbhandler = edit_db()