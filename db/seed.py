from db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO authors (name) VALUES (?)", ("Jane Doe",))
    cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", ("Tech Weekly", "Technology"))
    cursor.execute(
        "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
        ("AI Advances", "Content about AI.", 1, 1)
    )

    conn.commit()
    conn.close()
