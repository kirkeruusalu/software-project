import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from entities.user import User
from repositories.user_repository import user_repository


class UserService:
    """This class is responsible for application logic"""

    def __init__(self):
        self._user_repository = user_repository

    def create_user(self, username):
        is_there_user = self._user_repository.find_by_username(username)

        if is_there_user:
            raise ValueError("this username exists, choose a new one")
        
        user = self._user_repository.create_user(User(username))