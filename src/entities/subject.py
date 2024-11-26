class Subject:
    """
    Class describing a subject.

    Attributes:
        name (string) : Name of subject
        mastery_level : Beginner, Intermediate, or Advanced
    """

    def __init__(self, name, mastery_level="Beginner"):
        self.name = name
        self.mastery_level = mastery_level
        