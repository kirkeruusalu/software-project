import tkinter as tk
from tkinter import ttk
from services.user_service import user_service as usr_svc
from services.subject_service import SubjectService
from ui.views.ui_helpers import clear_status_label_after_delay

class UserSubjectsView(tk.Frame):
    """Class that displays all the subjects for a user

    """
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.subject_service = None
        self.create_widgets()

    def create_widgets(self):
        """Method that displays widgets for user to see
        """
        tk.Label(self, text = "Here you can see your added subjects, double-click on one to view details", font=("Helvetica", 14)).pack(pady=10)

        self.subjects_listbox = tk.Listbox(self, selectmode=tk.SINGLE, width=40, height=10)
        self.subjects_listbox.pack(pady=10)

        self.subjects_listbox.bind("<Double-1>", self.user_selection)

        tk.Button(self, text="Add Subject", 
                  command=lambda: self.switch_view("add_subject")).pack(pady=10)
        
        tk.Button(self, text="Visualize your subjects",
                  command=lambda: self.switch_view("visualizer")).pack(pady=10)

        tk.Button(self, text="Log out",
                  command=self.log_out).pack(pady=10)
        

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def display_user_subjects(self, data=None):
        """Method that displays the subjects for a user

        Args:
            data (message, optional): defaults to None.
        """
        current_user = self.user_service.current_user

        if not self.subject_service:
            self.subject_service = SubjectService(current_user)
        
        if data and "message" in data:
            self.status_label.config(text=data["message"], fg="green")
            clear_status_label_after_delay(self.status_label)
        

        self.subjects_listbox.delete(0, tk.END)
        subjects = self.subject_service.find_user_subjects()
        if subjects:
            for subject in subjects:
                self.subjects_listbox.insert(tk.END, f"{subject['name']}")
        else:
            self.subjects_listbox.insert(tk.END, "No subjects found.")
        
    def log_out(self):
        """Method that logs out a user in the UI
        """
        self.user_service.logout_user()
        self.switch_view("first")

    def user_selection(self, item):
        """Method for selecting a user
        """
        index = self.subjects_listbox.curselection()[0]
        selected_item = self.subjects_listbox.get(index)
        self.switch_view("subject_info", selected_item)

