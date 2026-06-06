import sqlite3


class SQLiteDB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            return self
        except sqlite3.Error as error:
            raise RuntimeError(f"Failed to open database {self.db_name}") from error

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            try:
                self.connection.close()
            except sqlite3.Error as close_error:
                print(f"Error: failed to close database connection: {close_error}")
        return False

    def execute(self, query, params=()):
        """Általános parancs futtatása (pl. CREATE TABLE)."""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        cursor.close()

    def write_single_record(self, table, record):
        """Egy rekord beszúrása dictionary-ből (kulcsok = oszlopnevek)."""
        columns = ", ".join(record.keys())
        placeholders = ", ".join("?" for _ in record)
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor = self.connection.cursor()
        cursor.execute(query, tuple(record.values()))
        self.connection.commit()
        cursor.close()