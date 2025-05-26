from db.connection import get_connection
from lib.models.article import Article

class Magazine:
    
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        rows = cursor.fetchall()
        conn.close()
        return [cls(*row) for row in rows]

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in rows]  # row has 5 fields now
