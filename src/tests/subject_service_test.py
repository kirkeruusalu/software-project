import unittest
from repositories.user_repository import UserRepository
from repositories.subject_repository import SubjectRepository
from entities . user import User
from services.user_service import UserService, PasswordWrongFormatError, AccountExistsError
from services.subject_service import SubjectService, SubjectAlreadyExistsError, TimeMustBeIntegerError


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

    def test_create_subject_already_exists(self):
        subject_name = "Math"
        mastery_level = "Intermediate"

        self.test_service.create_subject(subject_name, mastery_level)

        with self.assertRaises(SubjectAlreadyExistsError) as context:
            self.test_service.create_subject(subject_name, mastery_level)
        
        self.assertTrue("Subject already exists" in str(context.exception))

    def test_create_subject_no_name(self):
        subject_name = ""
        mastery_level = "Intermediate"

        with self.assertRaises(ValueError) as context:
            self.test_service.create_subject(subject_name, mastery_level)
        
        self.assertTrue("You have to enter a name" in str(context.exception))

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
    
    def test_delete_subject_not_found(self):
        subject_name = "History of horses"

        with self.assertRaises(ValueError) as context:
            self.test_service.delete_user_subject(subject_name)
        
        self.assertTrue("Subject not found" in str(context.exception))



    def test_update_mastery_level_success(self):
        subject_name = "Math"
        mastery_level = "Advanced"
        
        self.test_service.create_subject(subject_name, mastery_level)
        self.test_service.update_mastery_level(subject_name, "Beginner")

        new_mastery = self.test_service.get_mastery_level(subject_name)

        self.assertEqual(new_mastery, "Beginner")
    
    def test_log_time_spent_success(self):
        subject_name = "Math"
        mastery_level = "Advanced"
        
        self.test_service.create_subject(subject_name, mastery_level)
        self.test_service.log_time_spent(subject_name, 5)

        total_time = self.test_service.get_time_spent(subject_name)

        self.assertEqual(total_time, 5)

    def test_log_time_spent_not_integer(self):
        subject_name = "Math"
        mastery_level = "Advanced"
        
        self.test_service.create_subject(subject_name, mastery_level)

        with self.assertRaises(TimeMustBeIntegerError) as context:
            self.test_service.log_time_spent(subject_name, "abc")

        self.assertTrue("The time must be an integer" in str(context.exception))


    

    



