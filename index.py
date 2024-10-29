import tkinter as tk
from tkinter import simpledialog, messagebox
import os
import sys

# Define the password
PASSWORD = "Esrael"  # Change this to your desired password

def lock_screen():
    # Create the main window
    root = tk.Tk()
    root.title("Locked")
    
    # Set the window to full screen
    root.attributes("-fullscreen", True)
    root.configure(bg="black")

    # Create a label with a message
    label = tk.Label(root, text="This screen is locked!\nEnter password to unlock.", 
                     fg="white", bg="black", font=("Helvetica", 36))
    label.pack(expand=True)

    # Number of attempts
    attempts = 0

    # Function to unlock the screen
    def unlock():
        nonlocal attempts  # Use nonlocal to modify the attempts variable
        # Ask for the password
        user_input = simpledialog.askstring("Unlock", "Enter password:", show='*')
        if user_input == PASSWORD:
            root.destroy()  # Close the window if the password is correct
        else:
            attempts += 1
            messagebox.showerror("Error", "Incorrect password! Try again.")
            if attempts >= 3:  # Limit the number of attempts
                messagebox.showwarning("Warning", "Too many failed attempts. Exiting...")
                root.destroy()

    # Function to exit the application
    def exit_application(event):
        root.destroy()

    # Bind mouse click and Escape key
    root.bind("<Button-1>", lambda e: unlock())  # Click anywhere to trigger the password prompt
    root.bind("<Escape>", exit_application)  # Press Escape to exit

    # Run the application
    root.mainloop()

# Run the lock screen function
lock_screen()

# Instructions to set up the script to run on startup:
if sys.platform == "win32":
    # Windows
    startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
    script_name = os.path.basename(__file__)
    with open(os.path.join(startup_folder, f"{script_name}.bat"), 'w') as f:
        f.write(f'@echo off\npython "{os.path.abspath(__file__)}"\n')
    print("Startup script created in Windows Startup folder.")

elif sys.platform == "darwin":
    # macOS
    script_name = os.path.basename(__file__)
    os.system(f'osascript -e \'tell application "System Events" to make new login item at end with properties {{name:"LockScreen", path:"{os.path.abspath(__file__)}", visible:true}}\'')
    print("Startup script created in macOS Login Items.")

elif sys.platform == "linux":
    # Linux (GNOME example)
    autostart_path = os.path.expanduser("~/.config/autostart")
    os.makedirs(autostart_path, exist_ok=True)
    script_name = os.path.basename(__file__)
    with open(os.path.join(autostart_path, f"{script_name}.desktop"), 'w') as f:
        f.write(f"[Desktop Entry]\nType=Application\nName=LockScreen\nExec=python3 {os.path.abspath(__file__)}\n")
    print("Startup script created in Linux Autostart directory.")
