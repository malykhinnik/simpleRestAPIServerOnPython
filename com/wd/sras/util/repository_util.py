import sqlite3
from sqlite3 import Error
import sqlalchemy.pool


def __execute(cur, param, query):
    if param is None:
        cur.execute(query)
    else:
        cur.execute(query, param)


def create_connection_to_db(name):
    try:
        if name == ":memory:":
            # TODO This function has been deprecated, but I currently have no other solution
            sqlite = sqlalchemy.pool.manage(sqlite3, poolclass=sqlalchemy.pool.SingletonThreadPool)
            return sqlite.connect(name)
        else:
            return sqlite3.connect(name)
    except Error as e:
        print(e)
        return None


def fetchall(query, connection, param=None, close=True):
    try:
        cur = connection.cursor()
        __execute(cur, param, query)
        res = cur.fetchall()
        cur.close()
        return res
    except Error as e:
        print(e)
        return None
    finally:
        if close and connection:
            connection.close()


def fetchone(query, connection, param=None, close=True):
    try:
        cur = connection.cursor()
        __execute(cur, param, query)
        res = cur.fetchone()
        cur.close()
        return res
    except Error as e:
        print(e)
        return None
    finally:
        if close and connection:
            connection.close()


def execute(query, connection, param=None, close=True):
    try:
        cur = connection.cursor()
        __execute(cur, param, query)
        connection.commit()
        cur.close()
    except Error as e:
        print(e)
        return None
    finally:
        if close and connection:
            connection.close()
