import tkinter as tk
from tkinter import ttk
from ui.views.ui_helpers import clear_status_label_after_delay
from services.user_service import user_service as usr_svc

class CreateUserView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text = "Here you can create a new user").pack()

        tk.Label(self, text="New username").pack()
        self.username = tk.Entry(self)
        self.username.pack(pady=5)

        tk.Label(self, text="New password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack(pady=5)

        tk.Button(self, text="Submit", command=self.submit_user).pack(pady=10)

        tk.Button(self, text="Back to main",
                  command=lambda: self.switch_view("first")).pack()
        tk.Button(self, text = "Go to login",
                  command=lambda: self.switch_view("login")).pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def submit_user(self):
        username = self.username.get()
        password = self.password.get()

        try:
            self.user_service.create_user(username, password)
            self.status_label.config(text="User created!", fg="green")
            clear_status_label_after_delay(self.status_label)
        except ValueError as e:
            self.status_label.config(text=str(e), fg="red")
            clear_status_label_after_delay(self.status_label)
        except NameError as e:
            self.status_label.config(text=str(e), fg="red")
            clear_status_label_after_delay(self.status_label)
    