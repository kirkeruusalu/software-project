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

    def create_user(self, username):
        is_there_user = self._user_repository.find_by_username(username)

        if is_there_user:
            raise ValueError("this username exists, choose a new one")

        new = User(username)
        self._user_repository.create_user(new)
        self._current_user = new

    @property
    def current_user(self):
        return self._current_user
