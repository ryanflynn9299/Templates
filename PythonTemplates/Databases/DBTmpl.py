"""
SQLite DBC Template in Python
"""

import sqlite3
import json


class DB:
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
        except ConnectionRefusedError:
            self.conn = None

    def query(self):
        if not self.conn:
            return None

        return self.conn.execute("SELECT * FROM Example;")

    def select_id(self, id):
        query = f"SELECT Text FROM Example WHERE Id = {id};"
        cursor = self.conn.execute(query)
        return [row for row in cursor]

    def disconnect(self):
        self.conn.close()


def main():
    # configuration, ignore
    json_data = json.load(open("config.json", "r"))
    path = json_data["path"]

    # Actual DB operations
    db = DB(path)
    rows = db.select_id(1)
    print(' | '.join(rows[0]))


if __name__ == "__main__":
    main()
