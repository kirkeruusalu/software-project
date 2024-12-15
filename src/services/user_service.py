import string
import sys
import os.path
from entities.user import User
from repositories.user_repository import UserRepository

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class UserService:
    """This class is responsible for application logic"""

    def __init__(self, user_repository = UserRepository()):
        self._user_repository = user_repository
        self._current_user = None

    def _validate_password(self, password):
        """
        Validate the format of a password

        Args:
            password (str): The chosen password

        Raises:
            PasswordWrongFormatError: If the password does not meet the criteria

        Returns:
            True: If the password is valid
        """
        passw = str(password)
        numbers = list(string.digits)
        has_number = False

        for i in passw:
            if i in numbers:
                has_number = True

        if len(passw) < 5:
            raise PasswordWrongFormatError("Password too short")
        if not has_number:
            raise PasswordWrongFormatError("Password must contain a number")

        return True


    def validate_credentials(self, username, password):
        """Checks whether entered username exists and matches password

        Args:
            username (str): entered username
            password (str): entered password

        Raises:
            PasswordWrongFormatError: If the username and password dont match/it already exists

        Returns:
            True: If username and password match
        """
        is_there_user = self._user_repository.find_by_username(username)

        if is_there_user and is_there_user["password"] == password:
            return True

        raise PasswordWrongFormatError("Incorrect username or password")


    def create_user(self, username, password):
        """Creates a user with the chosen username and password

        Args:
            username (str): chosen username
            password (str): chosen password

        Raises:
            AccountExistsError: if the username was already found in the database
        """
        user = str(username)
        passw = str(password)

        is_there_user = self._user_repository.find_by_username(user)

        if is_there_user:
            raise AccountExistsError("This username exists, choose a new one")

        validation = self._validate_password(password)

        if validation:
            new = User(user, passw)
            self._user_repository.create_user(new)


    def login_user(self, username, password):
        """Logs in the user if credentials were valid

        Args:
            username (str): entered username 
            password (str): entered password

        Returns:
            User object: if login was successful, returns the current logged in user
            None: if login was unsuccessful
        """

        validate = self.validate_credentials(username, password)

        if validate:
            self._current_user = User(username, password)

        return self._current_user

    def logout_user(self):
        """Logs out the user
        """
        self._current_user = None

    @property
    def current_user(self):
        return self._current_user

user_service = UserService(UserRepository())

class PasswordWrongFormatError(Exception):
    """Exception class for wrong format password"""

class AccountExistsError(Exception):
    """Exception class for alr existing account"""
