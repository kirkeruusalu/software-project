from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """Class responsible for database operations on users
    """

    def __init__(self):
        self._connection = get_database_connection()

    def create_user(self, user=User):
        """Inserts a user object into the database

        Args:
            user (User object): contains the username and password to be added
        """
        cursor = self._connection.cursor()
        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password))
        self._connection.commit()

    def find_all_users(self):
        """Finds all the user in the database

        Returns:
            A list of tuples, each tuple is a database row with user info
        """
        cursor = self._connection.cursor()
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        return rows

    def find_by_username(self, username):
        """Finds from database by specific username

        Args:
            username (str): entered username

        Raises:
            ValueError: if anything other than a string is entetred

        Returns:
            A tuple with the user's username and password (database row)
        """
        if not isinstance(username, str):
            raise ValueError(
                f"Expected username to be a string, got {type(username)}")

        cursor = self._connection.cursor()
        cursor.execute(
            "select username, password from users where username = ?",
            (username,)
        )
        row = cursor.fetchone()
        return row

    def delete_all(self):
        """Deletes all users from the database
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from users")
        self._connection.commit()

    def delete_user(self, username):
        """Deletes the user with the specified username from the database
        """
        cursor = self._connection.cursor()

        cursor.execute("""
            delete from users where username=:c""", {"c": username})
        self._connection.commit()

user_repository = UserRepository()
