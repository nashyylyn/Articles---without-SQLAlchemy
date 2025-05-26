import os
from db.connection import get_connection

def setup_database():
    db_path = "db/database.db"
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = get_connection()
    cursor = conn.cursor()

    schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../db/schema.sql")
    with open(schema_path) as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)

    # Import seed_data inside function to avoid circular imports
    from db.seed import seed_data
    seed_data()

    conn.commit()
    conn.close()
    print("✅ Database setup and seeded successfully.")

if __name__ == "__main__":
    setup_database()
