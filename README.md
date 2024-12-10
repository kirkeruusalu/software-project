# Software Development, practical work

## Study Tracker Project
This project will be a simple tool to help manage progress across various subjects/skills.

Link to the week 5 release is [here](https://github.com/kirkeruusalu/software-project/releases/tag/viikko5)

Link to the week 6 release is [here](https://github.com/kirkeruusalu/software-project/releases/tag/viikko6)

## Documentation
You can find the timekeeping document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/timetracking.md). 

You can find the requirements specification document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/requirements_specification.md)

You can find the changelog document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/changelog.md)

You can find the architecture document [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/architecture.md)

You can find the user manual [here](https://github.com/kirkeruusalu/software-project/blob/main/documentation/user_manual.md)

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






