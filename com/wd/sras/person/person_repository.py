from com.wd.sras.util import repository_util


class Constant:
    db_name = "app.db"


def create_connection_to_app_db():
    return repository_util.create_connection_to_db(Constant.db_name)


def init():
    connection = create_connection_to_app_db()
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS person ("
                "id INTEGER NOT NULL CONSTRAINT person_pk PRIMARY KEY AUTOINCREMENT ,"
                "name TEXT NOT NULL,"
                "age INTEGER NOT NULL)")
    connection.commit()
    connection.close()


def exist(person_id):
    return repository_util.fetchone("SELECT EXISTS(SELECT 1 FROM person WHERE id=?)", create_connection_to_app_db(),
                                    str(person_id))


def create(name, age):
    if name is None or age is None:
        return None
    # If i understood correctly the doc: https://sqlite.org/faq.html#q5
    # SqlLite is threadsafe and two query in one connection it's not a problem
    connection = create_connection_to_app_db()
    repository_util.execute("INSERT INTO person (name, age) VALUES (?, ?)", connection, (name, age), False)
    return repository_util.fetchone("SELECT name, age, id FROM person WHERE id = last_insert_rowid()", connection)


def get_all():
    return repository_util.fetchall("SELECT name, age, id FROM person", create_connection_to_app_db())


def get(person_id):
    if person_id is None:
        return person_id
    return repository_util.fetchone("SELECT name, age, id FROM person WHERE id = ?", create_connection_to_app_db(),
                                    str(person_id))


def update(person_id, name, age):
    if id is None or name is None or age is None:
        return None
    connection = create_connection_to_app_db()
    repository_util.execute("UPDATE person SET name = (?), age = (?) WHERE id = (?)", connection,
                            (name, age, person_id), False)
    return repository_util.fetchone("SELECT name, age, id FROM person WHERE id = ?", connection, str(person_id))


def delete(person_id):
    repository_util.execute("DELETE FROM person WHERE id = ?", create_connection_to_app_db(), str(person_id))
