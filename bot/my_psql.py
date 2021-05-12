import psycopg2
from constants import conn, cur

conn.set_isolation_level(0)


def fetch_todo(user_id, task_id=None):
    if task_id:
        cur.execute(f"SELECT task FROM todo WHERE task_id='{task_id}'")
    else:
        cur.execute(f"SELECT task FROM todo WHERE status='p' AND user_id='{user_id}'")
    return cur.fetchall()


def add_todo(user_id, task):
    cur.execute(f"INSERT INTO todo (user_id, task, status) VALUES('{user_id}', '{task}', 'p')")
    conn.commit()
    return "OK"


def execute_sql(query):
    try:
        cur.execute(query)
        data = cur.fetchall()
        if data == []:
            conn.commit()
        return str(data) if data else "OK"

    except Exception as e:
        return str(e)
