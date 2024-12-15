# Software Development, practical work

## Study Tracker Project
This project is a simple tool to help manage progress across various subjects/skills.

Link to the final release is [here]().

Link to the week 5 release is [here](https://github.com/kirkeruusalu/software-project/releases/tag/viikko5)

Link to the week 6 release is [here](https://github.com/kirkeruusalu/software-project/releases/tag/viikko6)

## Python version
Python version 3.10.12 was used to create and test this project.

## Documentation
You can find the timekeeping document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/timetracking.md). 

You can find the requirements specification document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/requirements_specification.md)

You can find the changelog document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/changelog.md)

You can find the architecture document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/architecture.md)

You can find the user manual [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/user_manual.md)

You can find the testing document [here]().
## How to run the application:
Installing dependencies:
```
poetry install
```
Initialization:
```
poetry run invoke initialize
```
Starting the app:
```
poetry run invoke start
```
Running tests:
```
poetry run invoke test
```
Coverage report:
```
poetry run invoke coverage-report
```
Pylint: 
```
poetry run invoke lint
```

to do sunday:
- all of the documentation
- final release
- final tests
