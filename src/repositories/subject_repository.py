from entities.user import User
from entities.subject import Subject
from database_connection import get_database_connection


class SubjectRepository:
    """Class responsible for database operations on subjects

    """

    def __init__(self):
        self._connection = get_database_connection()

    def add_subject(self, user: User, subject: Subject):
        """Adds a subject related to the user into databse

        Args:
            user (User): given user
            subject (Subject): given subject
        """
        cursor = self._connection.cursor()
        cursor.execute("insert into subjects (username, name, mastery_level) values (?, ?, ?) ",
                (user.username, subject.name, subject.mastery_level))

        self._connection.commit()

    def find_subject_by_name(self, user: User, subject_name: str):
        """Finds a specific subject related to the user from databse

        Args:
            user (User): given user 
            subject_name (str): given subject

        Returns:
            A tuple of the found subject, None otherwise
        """
        cursor = self._connection.cursor()
        select = "select username, name, mastery_level from subjects where username=? and name=?"
        cursor.execute(select, (user.username, subject_name))

        row = cursor.fetchone()

        if row:
            return Subject(name=row[1], mastery_level=row[2])
        return None

    def find_all_subjects(self, user: User):
        """Finds all subjects related to the user from database

        Args:
            user (User): given user

        Returns:
            A list of tuples, where each tuple is a subject
        """
        cursor = self._connection.cursor()
        select = "select username, name, mastery_level from subjects where username = ? "

        cursor.execute(select, (user.username,))

        return cursor.fetchall()

    def delete_subject(self, user: User, subject: Subject):
        """Deletes the specified subject from the database

        Args:
            user (User): the given user
            subject (Subject): the given subject
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from subjects where user = ? and name = ? ",
                    (user.username, subject.name))
        self._connection.commit()

    def delete_all(self):
        """Deletes all subject objects from the database
        """
        cursor = self._connection.cursor()
        cursor.execute("delete from subjects")
        self._connection.commit()

subject_repository = SubjectRepository()
