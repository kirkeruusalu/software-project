import unittest
from repositories.subject_repository import SubjectRepository
from entities.user import User
from entities.subject import Subject

class TestSubjectRepository(unittest.TestCase):
    def setUp(self):
        self.test_repository = SubjectRepository()
        self.test_repository.delete_all()

        self.user_kirke = User("kirke")
        self.user_kirke2 = User("kirke2")
        self.subject_math = Subject("Math", "beginner")
        self.subject_science = Subject("Science", "intermediate")

    def test_add_subject(self):
        self.test_repository.add_subject(self.user_kirke, self.subject_math)
        found_subject = self.test_repository.find_subject_by_name(self.user_kirke, self.subject_math)

        self.assertIsNotNone(found_subject)
        self.assertEqual(found_subject[0], self.user_kirke.username)
        self.assertEqual(found_subject[1], self.subject_math.name)
        self.assertEqual(found_subject[2], self.subject_math.mastery_level)

    def test_find_subject_by_name_not_found(self):
        found_subject = self.test_repository.find_subject_by_name(self.user_kirke, self.subject_math)
        self.assertIsNone(found_subject)

    def test_add_multiple_subjects_for_same_user(self):
        self.test_repository.add_subject(self.user_kirke, self.subject_math)
        self.test_repository.add_subject(self.user_kirke, self.subject_science)
        math_found = self.test_repository.find_subject_by_name(self.user_kirke, self.subject_math)
        science_found = self.test_repository.find_subject_by_name(self.user_kirke, self.subject_science)

        self.assertIsNotNone(math_found)
        self.assertIsNotNone(science_found)

    def test_add_same_subject_for_different_users(self):
        self.test_repository.add_subject(self.user_kirke, self.subject_math)
        self.test_repository.add_subject(self.user_kirke2, self.subject_math)
        kirke_subject = self.test_repository.find_subject_by_name(self.user_kirke, self.subject_math)
        kirke2_subject = self.test_repository.find_subject_by_name(self.user_kirke2, self.subject_math)

        self.assertIsNotNone(kirke_subject)
        self.assertIsNotNone(kirke2_subject)

    def test_delete_all(self):
        self.test_repository.add_subject(self.user_kirke, self.subject_math)
        self.test_repository.add_subject(self.user_kirke2, self.subject_science)
        self.test_repository.delete_all()
        kirke_subject = self.test_repository.find_subject(self.user_kirke, self.subject_math)
        kirke2_subject = self.test_repository.find_subject(self.user_kirke2, self.subject_science)

        self.assertIsNone(kirke_subject)
        self.assertIsNone(kirke2_subject)

    def tearDown(self):
        self.test_repository.delete_all()

if __name__ == "__main__":
    unittest.main()
