from repositories.user_repository import UserRepository
from repositories.subject_repository import SubjectRepository
from services.user_service import UserService
from services.subject_service import SubjectService
from initialize_database import initialize_database

repository = UserRepository()
user = UserService()
subjectrepository =  SubjectRepository()
initialize_database()

print("here will be the future functionality of the program")

USERNAME = str(input("username: "))
user.create_user(USERNAME)
print("you have successfully created a new user")
print(f"Current user: {user.current_user.username}")  # Debug

current_user = user.current_user
subject = SubjectService(current_user)

SUBJECT = str(input("add a new subject: "))
MASTERY_LEVEL = str(input("add a mastery_level(default beginner)"))
subject.create_subject(SUBJECT, MASTERY_LEVEL)
print("you have successfully added a new subject")
