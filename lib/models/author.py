from db.connection import get_connection
from lib.models.article import Article
from lib.models.magazine import Magazine

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return cls(*row)
        else:
            return None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Article(*row) for row in rows]

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.id, m.name, m.category
            FROM magazines m
            JOIN articles a ON a.magazine_id = m.id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        conn.close()
        return [Magazine(*row) for row in rows]
