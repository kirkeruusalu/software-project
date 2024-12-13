import unittest
from repositories.user_repository import UserRepository
from repositories.subject_repository import SubjectRepository
from entities . user import User
from services.user_service import UserService, PasswordWrongFormatError, AccountExistsError
from services.subject_service import SubjectService, SubjectAlreadyExistsError


class TestSubjectService(unittest.TestCase):
    def setUp(self):
        self.test_subject_repository = SubjectRepository()
        self.test_user_repository = UserRepository()
        self.test_user_repository.delete_all()
        self.test_user = User("kirke", "password1")
        self.test_user_repository.create_user(self.test_user)

        self.test_service = SubjectService(self.test_user)
        self.test_subject_repository.delete_all()
    
    def test_create_subject_success(self):
        subject_name = "Math"
        mastery_level = "Beginner"

        self.test_service.create_subject(subject_name, mastery_level)

        subjects = self.test_subject_repository.find_all_subjects(self.test_user)
        self.assertEqual(len(subjects), 1)
        self.assertEqual(subjects[0][1], subject_name)
        self.assertEqual(subjects[0][2], mastery_level)

    def test_create_subject_unsuccessful(self):
        subject_name = "Math"
        mastery_level = "Intermediate"

        self.test_service.create_subject(subject_name, mastery_level)

        with self.assertRaises(SubjectAlreadyExistsError):
            self.test_service.create_subject(subject_name, mastery_level)

    def test_find_user_subjects(self):
        subject_1 = "Math"
        mastery_level_1 = "Beginner"
        subject_2 = "Horses"
        mastery_level_2 = "Intermediate"

        self.test_service.create_subject(subject_1, mastery_level_1)
        self.test_service.create_subject(subject_2, mastery_level_2)

        subjects = self.test_service.find_user_subjects()

        self.assertEqual(len(subjects), 2)
        self.assertEqual(subjects[0][1], subject_1)
        self.assertEqual(subjects[1][1], subject_2)

    def test_delete_subject_success(self):
        subject_name = "Math"
        mastery_level = "Beginner"

        self.test_service.create_subject(subject_name, mastery_level)

        self.test_service.delete_user_subject(subject_name)

        subjects = self.test_subject_repository.find_all_subjects(self.test_user)
        self.assertEqual(len(subjects), 0)


