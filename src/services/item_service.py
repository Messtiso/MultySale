from db.database import get_connection


def add_item(title, brand, category, size, condition, colour, price, photo_path):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT  INTO items (
            title, brand, category, size, condition, colour, price, photo_path
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (title, brand, category, size, condition, colour, price, photo_path))
    
    connection.commit()
    connection.close()


def get_all_items():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    connection.close()
    return items