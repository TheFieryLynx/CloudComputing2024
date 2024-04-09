from src.database.connector import connect
from src.models.user import User


def create_user(user: User):
    try:
        conn = connect()
    except Exception as e:
        print(f"Failed to connect to mysql database:", e)
        raise
    cursor = conn.cursor()
    query = "INSERT INTO users (email, first_name, last_name) VALUES (%s, %s, %s)"
    values = (user.email, user.firstName, user.lastName)
    try:
        cursor.execute(query, values)
        conn.commit()
    except Exception as e:
        print(f"Failed to execute query: ", e)
        raise
    result = cursor.lastrowid
    try:
        conn.close()
        cursor.close()
    except Exception as e:
        raise Exception(f"Failed to close mysql session:", e)
    return result


def get_user_by_id(user_id: int):
    try:
        conn = connect()
    except Exception as e:
        print(f"Failed to connect to mysql database:", e)
        raise
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    values = (user_id,)
    try:
        cursor.execute(query, values)
    except Exception as e:
        print(f"Failed to execute query:", e)
    result = []
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row)))
    try:
        conn.close()
        cursor.close()
    except Exception as e:
        print(f"Failed to close mysql session:", e)
        raise
    return result


def get_users():
    try:
        conn = connect()
    except Exception as e:
        print(f"Failed to connect to mysql database:", e)
        raise
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    try:
        cursor.execute(query)
    except Exception as e:
        print(f"Failed to execute query:", e)
    result = []
    columns = [column[0] for column in cursor.description]
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row)))
    try:
        conn.close()
        cursor.close()
    except Exception as e:
        print(f"Failed to close mysql session:", e)
        raise
    return result
