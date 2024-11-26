from entities.user import User
from entities.subject import Subject
from database_connection import get_database_connection


class SubjectRepository:
    """Class responsible for database operations on subjects

    """

    def __init__(self):
        self._connection = get_database_connection()

    def add_subject(self, user: User, subject: Subject):
        cursor = self._connection.cursor()
        cursor.execute("""
            insert into subjects 
                (username, name, mastery_level)
            values (?, ?, ?) """,
                (user.username, subject.name, subject.mastery_level))

        self._connection.commit()

    def find_subject(self, user: User, subject: Subject):
        cursor = self._connection.cursor()
        select = """
            select username, name, mastery_level
                from subjects where username=? and name=? and mastery_level=? """

        cursor.execute(select, (user.username, subject.name, subject.mastery_level))

        return cursor.fetchone()

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from subjects")
        self._connection.commit()

subject_repository = SubjectRepository()
