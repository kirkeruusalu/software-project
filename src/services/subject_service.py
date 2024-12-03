import sys
import os.path
from entities.user import User
from entities.subject import Subject
#from repositories.user_repository import UserRepository
from repositories.subject_repository import SubjectRepository

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class SubjectService:
    """This class is responsible for application logic"""

    def __init__(self, current_user: User):
        self._subject_repository = SubjectRepository()
        self._current_user = current_user

    def create_subject(self, name, mastery_level):

        subject_name = str(name)
        subject_level = str(mastery_level)

        new_subject = Subject(subject_name, subject_level)

        self._subject_repository.add_subject(self._current_user, new_subject)

    def find_user_subjects(self):
        return self._subject_repository.find_all_subjects(self._current_user)

    def delete_user_subject(self, name):

        subject_name = str(name)

        subject = self._subject_repository.find_subject_by_name(self._current_user, subject_name)

        if subject:
            self._subject_repository.delete_subject(self._current_user, subject)
        else:
            raise ValueError("Subject not found")
