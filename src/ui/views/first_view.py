import tkinter as tk
from tkinter import ttk

class FirstView(tk.Frame):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text = "This is the Subject Mastery Tracker application").pack()
        tk.Button(self, text = "Go to create user",
                  command=lambda: self.switch_view("create_user")).pack()
        tk.Button(self, text="Go to login",
                  command=lambda: self.switch_view("login")).pack()

    