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
        if row:
            return cls(row['id'], row['name'])
        return None

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = cursor.fetchall()
        return [Article(row['id'], row['title'], row['content'], row['author_id'], row['magazine_id']) for row in rows]

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.*
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        rows = cursor.fetchall()
        return [Magazine(row['id'], row['name'], row['category']) for row in rows]
