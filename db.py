import sqlite3

class DB:
    def __init__(self, db_file="items.db"):
        # Establish a connection to the database
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        # Create the items table if it doesn't exist already.
        # The url column is marked UNIQUE to avoid duplicate entries.
        create_table_query = """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            url TEXT UNIQUE
        );
        """
        self.conn.execute(create_table_query)
        self.conn.commit()

    def insert_item(self, title, price, url):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO items (title, price, url) VALUES (?, ?, ?)",
                (title, price, url)
            )
            self.conn.commit()
            print(f"Inserted item: {title}")
        except sqlite3.IntegrityError as e:
            # Handle duplicate URL insertion by rolling back the transaction
            print(f"Error inserting item with URL '{url}': {e}. Rolling back transaction.")
            self.conn.rollback()

    def get_all_items(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, title, price, url FROM items")
        return cursor.fetchall()

    def close(self):
        self.conn.close()
