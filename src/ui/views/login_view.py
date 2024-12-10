import tkinter as tk
from tkinter import ttk
from services.user_service import user_service as usr_svc

class LoginView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text = "Here you can log in to your account").pack()

        tk.Label(self, text="Username").pack()
        self.username = tk.Entry(self)
        self.username.pack(pady=5)

        tk.Label(self, text="Password").pack()
        self.password = tk.Entry(self, show="*")
        self.password.pack(pady=5)

        tk.Button(self, text="Log in", command=self.login_user).pack(pady=10)

        tk.Button(self, text="Back to main",
                  command=lambda: self.switch_view("first")).pack()
        #tk.Button(self, text = "Go to login",
         #         command=lambda: self.switch_view("login")).pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def login_user(self):
        username = self.username.get()
        password = self.password.get()

        try:
            self.user_service.login_user(username, password)
            self.switch_view("subjects")
        except NameError as e:
            self.status_label.config(text=str(e), fg="red")
    