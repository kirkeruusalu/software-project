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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=2)

        self.subject_name_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.subject_name_label.grid(row=0, column=0, columnspan=3, pady=10)

        
        self.mastery_level_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.mastery_level_label.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        self.log_time_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.log_time_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)

        self.mastery_levels = ["Beginner", "Intermediate", "Advanced"]
        self.selected_mastery = tk.StringVar()

        self.mastery_option_menu = tk.OptionMenu(self, self.selected_mastery, *self.mastery_levels)
        self.mastery_option_menu.grid(row=1, column=1, padx=10, pady=10)

        self.update_button = tk.Button(self, text="Update Mastery Level", command=self.update_mastery_level)
        self.update_button.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        self.time_entry = tk.Entry(self, font=("Helvetica", 12))
        self.time_entry.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.log_time_button = tk.Button(self, text="Log Time", command=self.log_time)
        self.log_time_button.grid(row=3, column=2, padx=10, pady=10, sticky="ew")

        tk.Button(self, text="Back",
                  command=lambda: self.switch_view("subjects")).grid(row=5, column=0, columnspan=1, pady=10, sticky="nsew")

        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=100, column=0, columnspan=2, pady=10)
    
    def display_subject(self, subject):
        current_user = self.user_service.current_user

        if not self.subject_service:
            self.subject_service = SubjectService(current_user)

        self.subject = self.subject_service.find_subject(subject)
        subject_name = self.subject[0]
        mastery_level = self.subject[1]
        time = self.subject[2]
        self.subject_name_label.config(text=f"Subject: {subject_name}")
        self.mastery_level_label.config(text=f"Mastery Level: {mastery_level}")
        self.log_time_label.config(text=f"Total time studying: {time}")

        self.selected_mastery.set(mastery_level)

    def update_mastery_level(self):
        new_level = self.selected_mastery.get()
        #subject = SubjectRepository()

        if self.subject:
            self.subject_service.update_mastery_level(self.subject[0], new_level)
            self.mastery_level_label.config(text=f"Mastery Level: {new_level}")
            self.status_label.config(text="Mastery changed successfully", fg="green")
            clear_status_label_after_delay(self.status_label)

    def log_time(self):

        subject = SubjectRepository()
        time = self.time_entry.get()
        if time and self.subject:
            self.subject_service.log_time_spent(self.subject[0], time)
            updated_total_time = self.subject_service.get_time_spent(self.subject[0])
            self.log_time_label.config(text=f"Total time studying: {updated_total_time}")
            #subject.check_subject_in_db(self.user_service.current_user.username)
            self.status_label.config(text="Time logged successfully", fg="green")








        

    
