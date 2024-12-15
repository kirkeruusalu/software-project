
## Structure of the application

The following package diagram shows the general architecture of the application.

![image](https://github.com/user-attachments/assets/c2c61340-11ef-4dcf-8f06-aa60357f1073)

## User Interface
The UI has 7 views:
1. Login
2. Create account
3. Main page
4. View subjects
5. Add subject
6. Subject overview
7. Visualize subjects

These views all have their own classes, only one can be viewed at a time. There is a view manager that manages switching between the views. All of the UI is in it's own directory, separate from the application logic.

## Application logic
Under the directory Entities, there are the two classes that make up the base of the application: User and Subject.

```mermaid
 classDiagram
      User "1" --> "*" Subject
      class User{
          username
          password
      }
      class Subject{
          name
          mastery_level
          time
      }
      
```


Under the directory Repositories are the classes that handle interactions with the database: UserRepository and SubjectRepository. These classes provide methods for the application to interact with the database, ensuring a separation between application logic and database, as well as between the UI.

Under the directory Services are the classes that handle the main application logic: UserService and SubjectService. These classes provide methods that are used to manage the overall logic behind the user interacting with the app. The UserService class makes use of the UserRepository class to interact with the database when it comes to creations of users, logging in/out etc. The SubjectService makes use of the SubjectRepository class to interact with the database (adding, removing, viewing, editing subjects).

Here is a package diagram showing how the repositories and services work.
![image](https://github.com/kirkeruusalu/software-project/blob/main/documentation/images/package_diagram_app.png)

## Storage of data
As mentioned earlier, the UserRepository and SubjectRepository handle data storage and interaction with the database. The database in use in my application is the SQLite database, and it has two tables (for User and Subject).
As one would expect, the users table holds in it all of the info about the user (with username and password as attributes). The subjects table holds in it all the info about the subjects (with id, username, name, mastery_level, time as attributes).

## Functionalities
The main functionalities are:

### Creating a user:
The user first from the main screen click on create user button. Then they are taken to a view, where they must input a username and a password. Here is the sequence diagram:

Sequence Diagram 
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepo
    participant Kirke
    User->>UI: User enters username and password
    UI->>UserService: create_user("kirke", "pass1")
    UserService->>UserRepo: find_by_username("kirke")
    UserRepo->>UserService: None
    UserService->>UserService: _validate_password("pass1")
    UserService->>UserService: True
    UserService->>Kirke: User("kirke", "pass1")
    UserService->>UserRepo: create_user(User)
    UI->>UI: create_user_view()

```

### Logging in a user:
Works very similarly to the create user. The user has to enter their credentials, and if they are correct, the user will be logged in and directed to a view of their subjects.

Sequence Diagram
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant UserService
    participant UserRepo
    participant Kirke
    User->>UI: User enters username and password
    UI->>UserService: login_user("kirke", "pass1")
    UserService->>UserService: validate_credentials("kirke", "pass1")
    UserService->>UserRepo: find_by_username("kirke")
    UserRepo->>UserService: True
    UserService->>Kirke: current_user = User("kirke", "pass1")
    UI->>UI: user_subjects_view()

```

### Viewing subjects:
Once the user has added a subject, they can either add another one, or click back to navigate to view of all subjects. This view is quite straight-forward, so a sequence diagram is not needed. This is the first view that shows up for the user once they have logged in. From here they can:
1. Click on add subject. Then the UI switches view into add_subject_view, that is described next in this file.
2. Double-click on a subject. Then the UI switches view into subject_info_view, which is also described later.
3. Click on visualize your subjects. Then the UI switches view into time_spent_view, which is described later.
4. Click on log out. Then the UI switches view into the first_view, which is simply the main screen where the user can either create an account or log into an existing one.

### Creating a new subject:
If user clicks on add subject, they will be directed to a screen where they can input the name and mastery level of a subject. When they click on submit, the UI calls the create_subject method from the SubjectService, giving it the name and mastery level as parameters. The create_subject method then makes sure that the subject name is not empty and a subject with the same name does not already exist. If that has been verified, then it calls the add_subject method from the SubjectRepository. That method will add a subject with the name and mastery level into the database, and the user will be given feedback of success (or failure if something was wrong at any step).

Sequence Diagram
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant SubjectService
    participant SubjectRepo
    User->>UI: User enters the name (and optionally mastery level) of subject
    UI->>SubjectService: create_subject(name)
    SubjectService->>SubjectService: find_subject(name)
    SubjectService->>SubjectRepo: find_subject_by_name(name)
    SubjectRepo->>SubjectService: None
    SubjectService->>SubjectRepo: add_subject(current_user, Subject(name, mastery_level, time))
    UI->>UI: add_subject_view() (also success message is displayed)

```
### Subject Overview/Edit:
If user enters the subject overview/edit view, they can see the mastery level and time logged for the subject. In this screen they can change these two, or they can choose to delete the subject. The following sequence diagram shows the functionality of updating mastery level.

Sequence Diagram
```mermaid
sequenceDiagram
    actor User
    participant UI
    participant SubjectService
    participant SubjectRepo
    User->>UI: User double-clicks on the subject they want to see.
    UI->>UI: subject_info_view()
    UI->>SubjectService: update_mastery_level(name, new_level)
    SubjectService->>SubjectService: find_subject(name)
    SubjectService->>SubjectRepo: find_subject_by_name(name)
    SubjectRepo->>SubjectService: (subject[1], subject[2], subject[3])
    SubjectService->>SubjectRepo: update_mastery(current_user, subject[0], new_level) e.g.(("kirke","pass1"), "math","Advanced")
    UI->>UI: same view remains, success message is displayed
```

### Other functionalities
1. The user can visualize their subjects, this uses matplotlib. A plot of time spent studying against subject names will be displayed, the plotting all happens in the user interface. In order to fetch the subjects, the UI calls the find_user_subjects() method from SubjectService. This in turn calls the find_all_subjects() method from SubjectRepository. This is sent back to the UI, where only the subject names and times are extracted from the repository's result.

2. The user can delete a subject. When the delete button is clicked, it calls the delete_user_subject() method from SubjecService, which in turns calls the delete_subject() method from SubjectRepository. The repository handles deletion in the database, and will go back to the UI where a message will be displayed.

3. As already mentioned in the subject overview/edit, the user can also log time. This functionality works almost identically to updating the mastery level, only there are rigurous checks to make sure that the time logged makes logical sense.

