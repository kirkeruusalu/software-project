import tkinter as tk
from tkinter import ttk
from services.user_service import user_service as usr_svc
from services.subject_service import SubjectService

class UserSubjectsView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.subject_service = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text = "Here you can see your added subjects").pack(pady=10)

        self.subjects_listbox = tk.Listbox(self, width=40, height=10)
        self.subjects_listbox.pack(pady=10)

        tk.Button(self, text="Add Subject", command=self.add_subject).pack(pady=10)

        tk.Button(self, text="Back to main",
                  command=lambda: self.switch_view("first")).pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def display_user_subjects(self):
        current_user = self.user_service.current_user

        if not self.subject_service:
            self.subject_service = SubjectService(current_user)

        self.subjects_listbox.delete(0, tk.END)
        subjects = self.subject_service.find_user_subjects()
        if subjects:
            for subject in subjects:
                self.subjects_listbox.insert(tk.END, f"{subject['name']} ({subject['mastery_level']})")
        else:
            self.subjects_listbox.insert(tk.END, "No subjects found.")
        
    def add_subject(self):
        self.switch_view("add_subject")
