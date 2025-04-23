import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="123456",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
SELECT u.username, s.score, s.level, s.saved_at
FROM user_score s
JOIN users u ON s.user_id = u.id
ORDER BY s.saved_at DESC;
""")

rows = cur.fetchall()

for row in rows:
    print(f"User: {row[0]}, Score: {row[1]}, Level: {row[2]}, Time: {row[3]}")

cur.close()
conn.close()