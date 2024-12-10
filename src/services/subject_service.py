import sys
import os.path
from entities.user import User
from entities.subject import Subject
#from repositories.user_repository import UserRepository
from repositories.subject_repository import SubjectRepository

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class SubjectService:
    """This class is responsible for the application logic related to subjects
    """

    def __init__(self, current_user: User):
        self._subject_repository = SubjectRepository()
        self._current_user = current_user

    def create_subject(self, name, mastery_level):
        """Creates a new subject for the current user

        Args:
            name (str): the name of the subject
            mastery_level (str): the mastery level, either beginner, intermediate, or advanced

        Raises:
            ValueError: if no subject name was entered
            SubjectAlreadyExistsError: if there is already a subject by that name
        """

        subject_name = str(name)
        subject_level = str(mastery_level)
        if not subject_name:
            raise ValueError("You have to enter a name")

        if not self.find_subject(subject_name):
            new_subject = Subject(subject_name, subject_level)
            self._subject_repository.add_subject(self._current_user, new_subject)

        else:
            raise SubjectAlreadyExistsError("Subject already exists")


    def find_user_subjects(self):
        """Finds all of the subjects related to the current user

        Returns:
            A list of the user's subjects as tuples
        """
        return self._subject_repository.find_all_subjects(self._current_user)

    def delete_user_subject(self, name):
        """Deletes the subject given as an argument from the current user

        Args:
            name (str): subject

        Raises:
            ValueError: if there was no subject by that name
        """

        subject_name = str(name)

        subject = self._subject_repository.find_subject_by_name(self._current_user, subject_name)

        if subject:
            self._subject_repository.delete_subject(self._current_user, subject)
        else:
            raise ValueError("Subject not found")

    def find_subject(self, name):
        """Finds a specific subject related to the current user

        Args:
            name (str): subject

        Returns:
            Subject object: if there was such a subject
        """
        subject_name = str(name)
        return self._subject_repository.find_subject_by_name(self._current_user, subject_name)


class SubjectAlreadyExistsError(Exception):
    """Exception raised when attempting to add a duplicate subject."""
    pass
