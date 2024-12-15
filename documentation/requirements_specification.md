# Requirements specification

## Purpose of the application
This application is a subject progress tracker to help users assess and keep track of their understanding of different subjects (this could also be applied to skills outside of academia). Users can input subjects and later edit them. For a user to use the application, they must create an account and sign in with valid credentials.

## Users
There is a regular user role, where the current user can create an account by choosing a username and password, and later log into the same account with their information saved. There can be several users.

## UI
The initial UI will be a command-line interface, which will be extended into a GUI as the project progresses. (GUI has been done)

## Functionalities
### Basic Functionalities
- When opening the application, the user will see a login screen, where they can either log in with their credentials or create a new account. (done)
- Once logged in, the user will be presented with a view of their current subjects and progress. (partly done)
- Users can add subjects and break them down into smaller subtopics (such as Computer Science -> Networks) (almost done)
- When a user adds a topic, it will automatically be assigned a skill level of beginner (the user can change this manually) (done)
- Users can log:
    - their perceived level of mastery in the subtopics (done)
    - how much time they have spent studying
    - any notes/comments they have about specific topics
- A simple chart can be generated that show how the user has progressed over time


### Possible future development ideas
- Creation of a root/admin user
- Providing a higher level of visualization
- Implementing a system that would suggest specific time intervals after which a certain subtopic should be reviewed
- The user can set specific time-based study goals
