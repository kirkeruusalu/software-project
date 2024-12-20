import tkinter as tk
from services.user_service import user_service as usr_svc
from services.subject_service import TimeMustBeIntegerError, TotalCantBeNegativeError
from services.subject_service import SubjectService
from ui.views.ui_helpers import clear_status_label_after_delay


class SubjectInfoView(tk.Frame):
    """Class responsible for viewing the info about a certain subject
    """
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.subject_service = None
        self.subject = None
        self.create_widgets()

    def create_widgets(self):
        """Method that creates widgets that user sees
        """
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
                  command=lambda: self.switch_view("subjects")).grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="sw")
        
        self.remove_subject_button = tk.Button(self, text="Delete subject", command=self.confirm_delete)
        self.remove_subject_button.grid(row=5, column=2, padx=10, columnspan=2, pady=10, sticky="se")

        self.status_label = tk.Label(self, text="")
        self.status_label.grid(row=100, column=0, columnspan=2, pady=10)
    
    def display_subject(self, subject):
        """Method that displays the user subjects

        Args:
            subject (str): the subject name
        """
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
        """Method that updates the mastery level of a subject 
        """
        new_level = self.selected_mastery.get()

        if self.subject:
            self.subject_service.update_mastery_level(self.subject[0], new_level)
            self.mastery_level_label.config(text=f"Mastery Level: {new_level}")
            self.status_label.config(text="Mastery changed successfully", fg="green")
            clear_status_label_after_delay(self.status_label)

    def log_time(self):
        """Method that logs time spent on a subject
        """
        time = self.time_entry.get()
        if time and self.subject:
            try:
                self.subject_service.log_time_spent(self.subject[0], time)
                updated_total_time = self.subject_service.get_time_spent(self.subject[0])
                self.log_time_label.config(text=f"Total time studying: {updated_total_time}")
                self.status_label.config(text="Time logged successfully", fg="green")
                clear_status_label_after_delay(self.status_label)
            except TimeMustBeIntegerError as e:
                self.status_label.config(text=str(e), fg="red")
                clear_status_label_after_delay(self.status_label)
            except TotalCantBeNegativeError as e:
                self.status_label.config(text=str(e), fg="red")
        
    def delete_subject(self):
        """Method that deletes subject for the user
        """
        if self.subject:
            self.subject_service.delete_user_subject(self.subject[0])


    def confirm_delete(self):
        """Method to confirm the deletion of a subject
        """
        window = tk.Toplevel(self)
        window.title("Confirm deleteion")
        window.geometry("300x150")
        window.transient(self)
        window.grab_set()

        tk.Label(window, text="Are you sure you want to delete?")

        def on_confirm():
            self.delete_subject()
            window.destroy()
            self.switch_view("subjects", data={"message" : "Subject deleted successfully", "fg" : "green"})

        
        def on_cancel():
            window.destroy()

        tk.Button(window, text="Yes", command=on_confirm, width=10).pack(side="left", padx=10, pady=20)
        tk.Button(window, text="Cancel", command=on_cancel, width=20).pack(side="right", padx=10, pady=20)








        

    
