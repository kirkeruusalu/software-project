import unittest
from repositories.user_repository import UserRepository
from entities . user import User

test_repository = UserRepository()


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        test_repository.delete_all()
        self.user_kirke = User("kirke", "password123")

    def test_create_user(self):
        test_repository.create_user(self.user_kirke)
        find_user = test_repository.find_by_username(self.user_kirke.username)

        self.assertEqual(find_user["username"], self.user_kirke.username)
