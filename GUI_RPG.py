# -*- coding: utf-8 -*-
"""
Header

@author: Christoph
Version : 0.1

History:
[2016.03.31, CS]: start with the basic layout of the GUI;
"""

import tkinter as tk

# create a new window
window = tk.Tk()
# set the window title
window.title("GUI: Ratten!")
# set the window size
window.geometry("600x300")
# set the window icon, must be in the same folder as the script
window.wm_iconbitmap('logo_black.ico')

def callback():
    #print("button clicked")
    w_status.configure(text="button clicked")

t_commands = "commands:\n'exit'\n'status'\n'mission'\n'go [north, east, south, west, up, down]'\n'get [item]'\n'fight [person]'\n'drop [item]'"
t_input = "hier schreibt der user seine Befehle"

# text field for the status
w_status = tk.Label(window, text="showStatus").pack(side="left")
# text field with the commands
w_commands = tk.Label(window, text=t_commands).pack(side="right")
# text for the input field
w_input = tk.Label(window, text=t_input).pack(side="bottom")
# input field itself
w_entry = tk.Entry(window).pack(side="bottom")
# button for the input field
w_button = tk.Button(window, text="Click me", command=callback).pack(side="bottom")


# draw the window and start the application
window.mainloop()