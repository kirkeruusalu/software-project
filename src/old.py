from repositories.user_repository import UserRepository
from repositories.subject_repository import SubjectRepository
from services.user_service import UserService
from services.subject_service import SubjectService
from initialize_database import initialize_database

repository = UserRepository()
user = UserService()
subjectrepository =  SubjectRepository()
initialize_database()

user_wish = str(input("Welcome! To create a user, press 1. To log in, press 2 "))

if user_wish == "1":
    USERNAME = str(input("username: "))
    PASSWORD = str(input("enter a password: "))
    user.create_user(USERNAME, PASSWORD)
    user.login_user(USERNAME, PASSWORD)

elif user_wish == "2":
    USERNAME = str(input("what is your username: "))
    PASSWORD = str(input("enter your password: "))
    user.login_user(USERNAME, PASSWORD)
    print(f"Current user: {user.current_user.username}")


current_user = user.current_user
subject = SubjectService(current_user)

SUBJECT = str(input("add a new subject: "))
MASTERY_LEVEL = str(input("add a mastery_level(default beginner)"))
subject.create_subject(SUBJECT, MASTERY_LEVEL)
print("you have successfully added a new subject")
