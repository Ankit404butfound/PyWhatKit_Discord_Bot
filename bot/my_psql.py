import psycopg2
from constants import conn, cur

conn.set_isolation_level(0)


def fetch_todo(user_id, task_id=None):
    cur.execute(f"SELECT task_id, task FROM todo WHERE status='p' AND user_id='{user_id}'")
    return cur.fetchall()


def add_todo(user_id, task):
    cur.execute(f"INSERT INTO todo (user_id, task, status) VALUES('{user_id}', '{task}', 'p')")
    conn.commit()
    return "OK"


def todo_done(task_id):
    try:
        cur.execute(f"UPDATE todo set status='d' WHERE task_id='{task_id}' and status='p'")
        conn.commit()
        return True
    except:
        return False


def log(user_id):
    cur.execute(f"SELECT task_id, task, status task FROM todo WHERE user_id='{user_id}'")
    return cur.fetchall()


def execute_sql(query):
    try:
        cur.execute(query)
        data = cur.fetchall()
        if data == []:
            conn.commit()
        return str(data) if data else "OK"

    except Exception as e:
        return str(e)
