"""
Digital Clock using Tkinter

This program creates a simple digital clock GUI application
that displays the current system time in HH:MM:SS format.
"""

# Import required modules
from tkinter import Tk, Label
import time


# -------------------- Window Setup --------------------

# Create main application window
app_window = Tk()

# Set window title
app_window.title("Digital Clock")

# Set window size (width x height)
app_window.geometry("420x150")

# Allow window resizing
app_window.resizable(1, 1)


# -------------------- Styling Configuration --------------------

# Font style for clock text
text_font = ("Boulder", 68, "bold")

# Background and foreground colors
background = "#f2e750"
foreground = "#363529"

# Border width around the label
border_width = 25


# -------------------- Label Widget --------------------

# Create label to display time
label = Label(
    app_window,
    font=text_font,
    bg=background,
    fg=foreground,
    bd=border_width
)

# Place label on window using grid layout
label.grid(row=0, column=1)


# -------------------- Clock Function --------------------

def digital_clock():
    """
    Fetches the current system time and updates the label
    every 200 milliseconds.
    """
    # Get current time in HH:MM:SS format
    current_time = time.strftime("%H:%M:%S")

    # Update label text
    label.config(text=current_time)

    # Call this function again after 200 milliseconds
    label.after(200, digital_clock)


# -------------------- Program Execution --------------------

# Start the clock
digital_clock()

# Run the Tkinter event loop
app_window.mainloop()
