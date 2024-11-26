from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Class responsible for database operations on users

    """

    def __init__(self):
        self._connection = get_database_connection()

    def create_user(self, user=User):
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username) values (?)",
            (user.username,))
        self._connection.commit()

    def find_all_users(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return rows

    def find_by_username(self, username):
        if not isinstance(username, str):
            raise ValueError(
                f"Expected username to be a string, got {type(username)}")

        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT username FROM users WHERE username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return row

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()


user_repository = UserRepository()
