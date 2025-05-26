from db.connection import get_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        rows = cursor.fetchall()
        conn.close()
        return [cls(row["id"], row["title"], row["content"], row["author_id"], row["magazine_id"]) for row in rows]
