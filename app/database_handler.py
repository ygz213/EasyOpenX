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

    def update_collection(self, orig_collectionname, collection_name, collection_apps):
        self.cursor.execute(f'''UPDATE database SET Collection = '{collection_name}', Apps = '{collection_apps}' WHERE Collection = '{orig_collectionname}' ''')
        self.database.commit()

    def delete_collection(self, collection_name):
        self.cursor.execute(f'''DELETE FROM database WHERE Collection = '{collection_name}' ''')
        self.database.commit()

    def check_collections(self):
        return self.cursor.execute('''SELECT Collection FROM database''').fetchall()

    def search_collection(self, collection_name):
        return self.cursor.execute(f'''SELECT * FROM database WHERE Collection = '{collection_name}' ''').fetchall()


dbhandler = edit_db()