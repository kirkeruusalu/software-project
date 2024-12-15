import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from services.subject_service import SubjectService
from services.user_service import user_service as usr_svc

class TimeSpentVisualizer(tk.Frame):
    """Class for visualizing the time spent against subjects, using matplotlib
    """
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        self.switch_view = switch_view
        self.user_service = usr_svc
        self.subject_service = None
        self.canvas = None
        self.create_widgets()

        parent.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_widgets(self):
        """Method that creates widgets for user to see
        """
        tk.Label(self, text="Time Spent on Subjects", font=("Helvetica", 14)).pack(pady=10)

        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(pady=10)

        tk.Button(self, text="Back to Subjects", command=lambda: self.switch_view("subjects")).pack(pady=10)
    
    def display_time_spent(self):
        """Method that displays the time spent on a task
        """
        current_user = self.user_service.current_user

        if not self.subject_service:
            self.subject_service = SubjectService(current_user)
        
        subjects = self.subject_service.find_user_subjects()
        subject_names = [subject[1] for subject in subjects]
        time_spent = [subject[3] for subject in subjects]
        
        self.plot_time_spent(subject_names, time_spent)

    def plot_time_spent(self, names, times):
        """
        Plots a bar chart of time spent on each subject.

        Args:
            names : subject names
            times : the times spent for each subject respectively
        """

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        fig, ax = plt.subplots(figsize=(6,2.5))
        ax.bar(names, times, color="blue")
        ax.set_xlabel("Subjects")
        ax.set_ylabel("Time Spent (hours)")
        ax.set_title("Time Spent on Subjects")
        ax.set_xticks(range(len(names)))
        ax.set_xticklabels(names, rotation=45)
        plt.tight_layout()

        self.canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
    
    def on_close(self):
        """Handle the window close event
        """
        self.quit() 
