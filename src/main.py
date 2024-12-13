import tkinter as tk
from ui.view_manager import ViewManager

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Subject Mastery Tracker")
    root.geometry("600x500")
    manager = ViewManager(root)
    manager.show_view("first")
    root.mainloop()
