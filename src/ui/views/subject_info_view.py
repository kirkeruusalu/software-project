import tkinter as tk
from tkinter import ttk
from services.user_service import user_service as usr_svc
from services.subject_service import SubjectService
from ui.views.ui_helpers import clear_status_label_after_delay
from repositories.subject_repository import SubjectRepository

class SubjectInfoView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.subject_service = None
        self.subject = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text = "Subject Details").pack(pady=10)

        self.subject_name_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.subject_name_label.pack(pady=10)

        self.mastery_level_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.mastery_level_label.pack(pady=5)

        self.mastery_levels = ["Beginner", "Intermediate", "Advanced"]
        self.selected_mastery = tk.StringVar()

        self.mastery_option_menu = tk.OptionMenu(self, self.selected_mastery, *self.mastery_levels)
        self.mastery_option_menu.pack(pady=10)

        self.update_button = tk.Button(self, text="Update Mastery Level", command=self.update_mastery_level)
        self.update_button.pack(pady=10)

        tk.Button(self, text="Back",
                  command=lambda: self.switch_view("subjects")).pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()
    
    def display_subject(self, subject):
        current_user = self.user_service.current_user

        if not self.subject_service:
            self.subject_service = SubjectService(current_user)

        self.subject = self.subject_service.find_subject(subject)
        subject_name = self.subject[0]
        mastery_level = self.subject[1]
        self.subject_name_label.config(text=f"Subject: {subject_name}")
        self.mastery_level_label.config(text=f"Mastery Level: {mastery_level}")
        self.selected_mastery.set(mastery_level)

    def update_mastery_level(self):
        new_level = self.selected_mastery.get()
        subject = SubjectRepository()

        if self.subject:
            self.subject_service.update_mastery_level(self.subject[0], new_level)
            subject.check_subject_in_db("kirke")
            self.mastery_level_label.config(text=f"Mastery Level: {new_level}")
            self.status_label.config(text="Mastery changed successfully", fg="green")
            clear_status_label_after_delay(self.status_label)




        

    
