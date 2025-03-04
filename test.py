import shutil, os, webbrowser, subprocess, winreg, tkinter as tk, time, ctypes, urllib.request


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

subprocess.run(['cleanmgr', '\sagerun:1'], shell=True)

subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\DWM', '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)

subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search', '/v', 'CortanaConsent', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)

subprocess.run(['reg', 'add', 'HKCU\\Control Panel\\Desktop', '/v', 'WindowAnimation', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)







import ctypes
import urllib.request
import os

def change_wallpaper():
    # URL of the image you want to use as wallpaper
    image_url = "https://www.boredpanda.com/blog/wp-content/uploads/2024/01/funny-weird-some-images-10-659bfc19cb0bf-png__700.jpg"
    
    # Path where the image will be saved temporarily
    image_path = os.path.join(os.getenv('TEMP'), "temp_wallpaper.jpg")
    
    # Download the image to a temporary file
    try:
        urllib.request.urlretrieve(image_url, image_path)
        print("Image downloaded successfully.")
    except Exception as e:
        print(f"Error downloading image: {e}")
        return

    # Set the downloaded image as the wallpaper
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        print("Wallpaper changed successfully.")
    except Exception as e:
        print(f"Error setting wallpaper: {e}")
    
    # Optionally, delete the temporary image file after setting the wallpaper
    os.remove(image_path)

# Run the function to change the wallpaper
change_wallpaper()

