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

    def update_mastery_level(self, name, new_level):
        """Updates the mastery level for a subject

        Args:
            name (str): name of the subject
            new_level (str): new mastery level, beginner intermediate or advanced
        """
        subject = self.find_subject(name)

        self._subject_repository.update_mastery(self._current_user, subject[0], new_level)

    def log_time_spent(self, name, new_time):
        """Adds to the total time spent studying a subject

        Args:
            name (str): name of subject
            old_time (int): the previous time
            new_time (int): the added time
        """
        subject = self.find_subject(name)

        try:
            new_time = int(new_time)
        except ValueError as exc:
            raise TimeMustBeIntegerError("The time must be an integer.") from exc

        total = int(subject[2]) + int(new_time)
        if total < 0:
            raise TotalCantBeNegativeError("The total time cant be negative")
        self._subject_repository.log_time(self._current_user, subject[0], total)

    def get_time_spent(self, name):
        """Retrieves the total time logged by user for subject

        Args:
            name (str): name of subject

        Returns:
            time (int): returns the third value from the corresponding database row
        """
        subject = self.find_subject(name)
        return subject[2]

    def get_mastery_level(self, name):
        """Retrieves the mastery_level for the given subject

        Args:
            name (str): name of subject

        Returns:
            mastery_level (str): returns the second value from the corresponding database row
        """
        subject = self.find_subject(name)
        return subject[1]

class SubjectAlreadyExistsError(Exception):
    """Exception raised when attempting to add a duplicate subject."""

class TimeMustBeIntegerError(Exception):
    """Excpetion raised when attempting to input a non-integer into time"""

class TotalCantBeNegativeError(Exception):
    """Exception raised when deleting too much time from time logged"""
