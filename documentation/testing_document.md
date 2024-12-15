# Testing Document

 This application has been tested extensively manually with system testing, as well as with automated unittests.

 ## Unittests

### Application Logic
The UserService is tested with TestUserService class. SubjectService is tested with TestSubjectService class. They use a test instance of the UserRepository and SubjectRepository.

### Application Repositories
The UserRepository is tested with the TestUserRepository class, and the SubjectRepository is tested with the TestSubjectRepository class. Both use a temporary SQLite database created just for testing. The test database file name is specified in the .env.test file at the application root.

### Test coverage
The coverage of the unittests (without the UI and the database and configuration files) is at 96%.


![image](https://github.com/kirkeruusalu/software-project/blob/main/documentation/images/coverage_report.png)

## System testing

I performed the systemic testing of the application manually. 

### Installing and configuration
The instructions in the README.md file as well as the user manual have been followed, and the application worked as expected. The application has been tested with an already existing database, as well as a newly created one at the opening of the application.

### Testing of functionalities
The application has been manually tested extensively, trying to put invalid inputs into all fields, and making sure that the correct error messages are shown, and that overall everything works in the way the user would expect it to.

## Problems still present
It would perhaps been wiser to use a MockRepository when testing the UserService and SubjectService. This way it could be made sure that the application logic is completely separated from repository logic for testing.
Another thing to consider would be adding test coverage for edge cases, as currently there are a couple missing.



 
 
