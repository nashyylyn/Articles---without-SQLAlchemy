from db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()


    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Doe",))
    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("John Smith",))

    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Health Today", "Health"))

    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                   ("AI Advances", 1, 1))
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                   ("Wellness Tips", 2, 2))

    conn.commit()
    conn.close()
