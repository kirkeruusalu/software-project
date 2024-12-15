class User:
    """
    Class describing an individual user.

    Attributes:
        username (str): A unique username 
        password (str): A password with certain criteria

    Methods:
        __eq__(other): Check if another User instance is equal to current one.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username and self.password == other.password
        return False
