import psycopg2
from constants import conn, cur
import time
from time_zones import IST

conn.set_isolation_level(0)


def fetch_todo(user_id, task_id=None):
    cur.execute(f"SELECT task_id, task FROM todo WHERE status='p' AND user_id='{user_id}'")
    return cur.fetchall()


def add_todo(user_id, task):
    YYYY, MM, DD, HH, MI, SS = IST()
    cur.execute(f"INSERT INTO todo (user_id, task, status, assigned_time) VALUES('{user_id}', '{task}', 'p', '{YYYY}-{MM}-{DD}-{HH}-{MI}-{SS}')")
    conn.commit()
    return "ADDED"


def todo_done(task_id):
    try:
        cur.execute(f"UPDATE todo set status='d' WHERE task_id='{task_id}' and status='p'")
        conn.commit()
        return True
    except:
        return False


def log(user_id):
    cur.execute(f"SELECT task_id, task, status, assigned_time FROM todo WHERE user_id='{user_id}'")
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
