import tkinter as tk

def clear_status_label_after_delay(widget, delay=2000):
    """
    Clears the text of a Tkinter Label widget after a specified delay.

    Args:
        widget: The Tkinter Label widget to clear.
        delay: Time in milliseconds to wait before clearing the label (default: 1000ms).
    """
    widget.after(delay, lambda: widget.config(text=""))
