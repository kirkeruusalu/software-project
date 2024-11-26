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
