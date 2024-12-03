import tkinter as tk
from ui.views.first_view import FirstView
from ui.views.create_user_view import CreateUserView
from ui.views.login_view import LoginView
from ui.views.user_subjects_view import UserSubjectsView
from ui.views.add_subject_view import AddSubjectView

class ViewManager:
    def __init__(self, root):
        self.root = root
        self.views = {}
        self.current_view = None
        self.initialize_view()

    def initialize_view(self):
        self.views["first"] = FirstView(self.root, self.show_view)
        self.views["create_user"] = CreateUserView(self.root, self.show_view)
        self.views["login"] = LoginView(self.root, self.show_view)
        self.views["subjects"] = UserSubjectsView(self.root, self.show_view)
        self.views["add_subject"] = AddSubjectView(self.root, self.show_view)

    def show_view(self, view):
        if self.current_view:
            self.current_view.pack_forget()

        self.current_view = self.views[view]
        self.current_view.pack(fill="both")

        if isinstance(self.current_view, UserSubjectsView):
            self.current_view.display_user_subjects()
