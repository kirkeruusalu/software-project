import tkinter as tk
from tkinter import ttk
from ui.views.ui_helpers import clear_status_label_after_delay
from services.user_service import user_service as usr_svc
from services.subject_service import SubjectService, SubjectAlreadyExistsError

class AddSubjectView(tk.Frame):
    """Class responsible for the view the user sees when adding a subject

    """
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.subject_service = None
        self.user_service = usr_svc
        self.create_widgets()

    def create_widgets(self):
        """Creates widgets that display on the screen
        """
        tk.Label(self, text="Enter new subject details").pack(pady=10)

        tk.Label(self, text="Subject Name").pack()
        self.subject_name = tk.Entry(self)
        self.subject_name.pack(pady=5)

        tk.Label(self, text="Mastery Level").pack()
        self.mastery_level = ttk.Combobox(self, values=["Beginner", "Intermediate", "Advanced"])
        self.mastery_level.set("Beginner")
        self.mastery_level.pack(pady=5)

        tk.Button(self, text="Add new subject", command=self.add_subject).pack(pady=10)
        tk.Button(self, text="Back", command=lambda: self.switch_view("subjects")).pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()


    def add_subject(self):
        """Adds subject that the user inputs (if no errors)
        """
        subject_name = self.subject_name.get()
        mastery_level = self.mastery_level.get()

        if not self.subject_service:
            self.subject_service = SubjectService(self.user_service.current_user)
        
        try:
            self.subject_service.create_subject(subject_name, mastery_level)
            self.status_label.config(text="Subject added successfully", fg="green")
            clear_status_label_after_delay(self.status_label)
        except ValueError as e:
            self.status_label.config(text=str(e), fg="red")
            clear_status_label_after_delay(self.status_label)
        except SubjectAlreadyExistsError as e:
            self.status_label.config(text=str(e), fg="red")
            clear_status_label_after_delay(self.status_label)
