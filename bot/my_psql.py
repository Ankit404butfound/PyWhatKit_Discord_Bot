import psycopg2
from constants import conn, cur

conn.set_isolation_level(0)


def fetch_todo():
    cur.execute("SELECT * FROM todo WHERE status='todo'")
    return cur.fetchall()


def execute_sql(query):
    try:
        cur.execute(query)
        data = cur.fetchall()
        if data == []:
            conn.commit()
        return data if data else "OK"

    except Exception as e:
        return str(e)
