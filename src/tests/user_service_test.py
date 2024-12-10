import unittest
from repositories.user_repository import UserRepository
from entities . user import User
from services.user_service import UserService, PasswordWrongFormatError, AccountExistsError

test_repository = UserRepository()

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.test_service = UserService(test_repository)
        test_repository.delete_all()
    
    def test_create_user(self):
        self.test_service.create_user("kirke", "password1")
        
        user = test_repository.find_by_username("kirke")

        self.assertEqual(user["username"], "kirke")

    def test_validate_password_success(self):
        valid = self.test_service._validate_password("password1")

        self.assertEqual(valid, True)

    def test_validate_password_too_short(self):
        with self.assertRaises(Exception) as context:
            self.test_service._validate_password("hi3")

        self.assertTrue("Password too short" in str(context.exception))

    def test_validate_password_no_number(self):
        with self.assertRaises(Exception) as context:
            self.test_service._validate_password("passworddddd")

        self.assertTrue("Password must contain a number" in str(context.exception))

    def test_validate_credentials_success(self):
        self.test_service.create_user("kirke", "password1")
        valid = self.test_service.validate_credentials("kirke", "password1")

        self.assertEqual(valid, True)

    def test_validate_credentials_incorrect(self):
        self.test_service.create_user("kirke", "password1")
        with self.assertRaises(Exception) as context:
            self.test_service.validate_credentials("kirke", "password2")

        self.assertTrue("Incorrect username or password" in str(context.exception))