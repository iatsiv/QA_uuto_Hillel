import psycopg2

class BaseRepository:
    def __init__(self):
        self._connection = psycopg2.connect(
            user='postgres',
            password='1234',
            host='127.0.0.1',
            port='5432',
            database='hillel'
        )
        self._connection.set_session(autocommit=True)
        self._cursor = self._connection.cursor()


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()

    def get_all_users(self):
        self._cursor.execute("SELECT * FROM users;")
        return self._cursor.fetchall()

    def get_user_by_id(self, user_id):
        self._cursor.execute(f"SELECT * FROM users WHERE id = {user_id};")
        return self._cursor.fetchone()

    def insert_user(self, id, first_name, last_name, email, phone, status):
        self._cursor.execute(
            f"INSERT INTO users(id, first_name, last_name, email, phone, status) "
            f"VALUES ('{id}', '{first_name}', '{last_name}', '{email}', '{phone}', '{status}');")

    def delete_by_id(self, user_id):
        self._cursor.execute(f"DELETE FROM users WHERE id = {user_id};")

    def update_user_by_id(self, user_id, first_name, last_name, email, phone, status):
        self._cursor.execute(
            f"UPDATE users SET first_name = '{first_name}', last_name = '{last_name}', email = '{email}', "
            f"phone = '{phone}', status = '{status}' WHERE id = {user_id};"
        )

if __name__ == "__main__":
    rep = UserRepository()
    rep.insert_user(17, "Fifth",  "Viviod", "dsdf342@sdzz.ckc", "+380976545566", 1)
    rep.delete_by_id(17)
    rep.update_user_by_id(2, "Olena", "Kapustenko", "updateded@example.com", "+1234567890", 1)
    print(rep.get_all_users())
    print(rep.get_user_by_id(2))
