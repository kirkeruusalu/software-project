# Requirements specification

## Purpose of the application
This application is a subject progress tracker to help users assess and keep track of their understanding of different subjects (this could also be applied to skills outside of academia). Users can input subjects and later edit them. For a user to use the application, they must create an account and sign in with valid credentials.

## Users
There is a regular user role, where the current user can create an account by choosing a username and password, and later log into the same account with their information saved. There can be several users.

## UI
The UI is a graphic userface, using the Tkinter library.

## Functionalities
### Basic Functionalities
- When opening the application, the user will see a screen prompting them to either go to log in or go to create account.
    - If they chose create account, they must make a unique username and a password. The password must be at least 5
      characters long and include a number.
    - If they chose log in, they must type in the correct credentials.
- Once logged in, the user will be presented with a view of their current subjects. They can (double)click on each of the subjects to view more info. 
- Users can add subjects and add a mastery level (beginner, intermediate, or advanced). It will automatically be assigned a level of beginner.
- When updating a subject, users can log:
    - their perceived level of mastery in the subtopics 
    - how much time they have spent studying. They can also subtract time, but the time can never be negative
- A simple chart can be generated that shows bar charts of how much time they have spent on each subject.
- The user can deleted a subject as well, during which a pop-up screen will ask them for confirmation if they are sure they want to delete it.
- The user can log out, after which they will be redirected to the main page. There they can log in again, or create a new account. Their old log-in details are saved in the database.


### Possible future development ideas
- Creation of a root/admin user
- Providing a higher level of visualization
- Implementing a system that would suggest specific time intervals after which a certain subtopic should be reviewed
- The user can set specific time-based study goals
