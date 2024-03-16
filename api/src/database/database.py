from src.database.connector import connect
from src.models.user import User


def create_user(user: User):
    try:
        conn = connect()
    except Exception as e:
        raise Exception(f"Failed to connect to mysql database: {e}")
    cursor = conn.cursor()
    query = "INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)"
    values = (user.email, user.firstName, user.lastName)
    try:
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        raise Exception(f"Failed to execute query: {e}")
    try:
        conn.close()
    except Exception as e:
        raise Exception(f"Failed to close mysql session: {e}")
    return cursor.lastrowid
