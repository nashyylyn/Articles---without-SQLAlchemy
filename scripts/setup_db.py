import os
from db.connection import get_connection  

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    schema_path = os.path.join(os.path.dirname(__file__), '../db/schema.sql')  

    if not os.path.exists(schema_path):
        raise FileNotFoundError(f"Schema file not found at {schema_path}")

    with open(schema_path, 'r') as f:
        schema_sql = f.read()

    cursor.executescript(schema_sql)
    conn.commit()

    
    cursor.execute("INSERT INTO authors (name) VALUES ('Jane Doe')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Weekly', 'Technology')")
    cursor.execute("INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
                   ('AI Advances', 'Content about AI', 1, 1))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete!")
