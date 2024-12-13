class Subject:
    """
    Class describing a subject.

    Attributes:
        name (str) : Name of subject
        mastery_level (str) : Beginner, Intermediate, or Advanced
        time (int)    : Time spent studying the subject
    """

    def __init__(self, name, mastery_level="Beginner", time=0):
        self.name = name
        self.mastery_level = mastery_level
        self.time = time
        