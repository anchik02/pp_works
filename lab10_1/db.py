import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="123456",
        host="localhost",
        port="5432"
    )

def get_or_create_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id

def save_score(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()