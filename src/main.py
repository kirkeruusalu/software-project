from repositories.user_repository import UserRepository
from initialize_database import initialize_database
from services.user_service import UserService

repository = UserRepository()
user = UserService()
initialize_database()

print("here will be the future functionality of the program")

USERNAME = str(input("username: "))
user.create_user(USERNAME)
print("you have successfully created a new user")
