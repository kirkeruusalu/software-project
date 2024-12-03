## Class Diagram

![image](https://github.com/user-attachments/assets/c2c61340-11ef-4dcf-8f06-aa60357f1073)

## Sequence Diagram for create user functionality
```mermaid
sequenceDiagram
    participant UI as User Interface
    participant US as UserService
    participant UR as UserRepository

    UI->>UI: User enters username and password
    UI->>US: Call create_user(username, password)
    US->>UR: Call create_user(user)
    UR->>UR: Store user data in database
    UR->>US: Return success
    US->>UI: Notify user creation success
```


