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


def update_item_status(item_id, status):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE items
        SET status = ?
        WHERE id = ?
    """, (status, item_id))

    connection.commit()
    connection.close()


def mark_item_as_sold(item_id, sold_price, sold_platform):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE items
        SET status = 'sold',
            sold_price = ?,
            sold_platform = ?
        WHERE id = ?
    """, (sold_price, sold_platform, item_id))

    connection.commit()
    connection.close()


def update_item_field(item_id, field_name, new_value):
    allowed_fields = [
        "title", "brand", "category", "size", "condition", "colour", "price", "photo_path", "status", "listed_platforms", "sold_price", "sold_platforms"
    ]

    if field_name not in allowed_fields:
        print("Invalid field selected.")
        return
    
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"""
        UPDATE items
        SET {field_name} = ?
        WHERE id = ?
    """, (new_value, item_id))

    connection.commit()
    connection.close()