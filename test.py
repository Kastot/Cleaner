import shutil, os, webbrowser, subprocess, time, ctypes, urllib.request, tkinter as tk
from plyer import notification
import tkinter as tk
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import sys

import shutil, os, webbrowser, subprocess, time, ctypes, urllib.request, tkinter as tk
from plyer import notification
import tkinter as tk
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle
import sys

import requests
from pynput import keyboard








###################################################################################

def check_and_install_python():
    try:
       
        subprocess.run(['python', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python is already installed.")
    except subprocess.CalledProcessError:
        print("Python not found. Installing Python...")

       
        python_installer_url = "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe"  
        installer_path = "python_installer.exe"
        urllib.request.urlretrieve(python_installer_url, installer_path)

     
        subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)

        print("Python installation complete.")
        os.remove(installer_path)  #


###################################################################################

def run_cleanup_script(progress_callback):
    DelTemp = 'c:\\windows\\Temp'
    for filename in os.listdir(DelTemp):
        file_path = os.path.join(DelTemp, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        progress_callback()

    ###################################################################################

    DelBin = 'C:\\$Recycle.Bin'
    for filename in os.listdir(DelBin):
        file_path = os.path.join(DelBin, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        progress_callback()

    ###################################################################################

    DelLogs = 'C:\\Windows\\Logs'
    for filename in os.listdir(DelLogs):
        file_path = os.path.join(DelLogs, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        progress_callback()

    ###################################################################################

    subprocess.run(['cleanmgr', '/sagerun:1'], shell=True)
    subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\DWM', '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)
    subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search', '/v', 'CortanaConsent', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)
    subprocess.run(['reg', 'add', 'HKCU\\Control Panel\\Desktop', '/v', 'WindowAnimation', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)

    registry_settings = [
        ('HKCU\\Control Panel\\Desktop', 'MenuShowDelay', 'REG_SZ', '0'),
        ('HKCU\\Control Panel\\Desktop', 'WindowAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'ComboBoxAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'SmoothScroll', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'CursorShadow', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'MenuFade', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'SelectionFade', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'ToolTipAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'ToolTipFade', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'IconsOnly', 'REG_DWORD', '1'),
        ('HKCU\\Software\\Microsoft\\Windows\\DWM', 'EnableAeroPeek', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'TaskbarAnimations', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop\\WindowMetrics', 'MinAnimate', 'REG_SZ', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'MenuAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'ToolTipAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'ListviewAlphaSelect', 'REG_DWORD', '0'),
        ( 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'ListviewShadow', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'ListviewWatermark', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'TaskbarAnimations', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'TaskbarTransparency', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'StartButtonBalloonTip', 'REG_DWORD', '0'),
        
    ]
    for key, value_name, value_type, value_data in registry_settings:
        subprocess.run(['reg', 'add', key, '/v', value_name, '/t', value_type, '/d', value_data, '/f'], shell=True)

###################################################################################

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.title = "Emi's Cleaner"
        self.icon = 'Rake.ico'
        with layout.canvas.before:
            Color(0x12/255, 0x07/255, 0x20/255, 1)
            self.rect = Rectangle(size=(layout.width, layout.height), pos=layout.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        self.label = Label(text="Click the button to clean your system", font_size=32, color=(1, 1, 1, 1))
        layout.add_widget(self.label)

        button = Button(
            text="Run Cleanup Script",
            size_hint=(None, None),
            size=(140, 50), padding=(10, 1),
            background_color=(0.945, 0.769, 0.059, 1.0)
        )
        button.bind(on_press=self.on_click)
        layout.add_widget(button)

        # "My Site" button
        my_site_button = Button(
            text="My Site",
            size_hint=(None, None),
            size=(75, 50), padding=(10, 1),
            background_color=(0.945, 0.769, 0.059, 1.0)
        )
        my_site_button.bind(on_press=self.open_site)
        layout.add_widget(my_site_button)

        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_click(self, instance):
        self.label.text = "Cleaning in progress..."
        run_cleanup_script(lambda: None) 
        self.label.text = "Your computer is cleaner now, have a great day. --Emi."
    
    def open_site(self, instance):
        webbrowser.open("http://codescribe.tilda.ws")  

if __name__ == "__main__":

    check_and_install_python()


    MyApp().run()

###################################################################################




###################################################################################

def check_and_install_python():
    try:
        # Try to check if Python is installed
        subprocess.run(['python', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python is already installed.")
    except subprocess.CalledProcessError:
        print("Python not found. Installing Python...")

        # Download Python installer
        python_installer_url = "https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe"  # Update this URL to the latest version
        installer_path = "python_installer.exe"
        urllib.request.urlretrieve(python_installer_url, installer_path)

        # Run installer silently
        subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)

        print("Python installation complete.")
        os.remove(installer_path)  # Remove installer after installation


###################################################################################

def run_cleanup_script(progress_callback):
    DelTemp = 'c:\\windows\\Temp'
    for filename in os.listdir(DelTemp):
        file_path = os.path.join(DelTemp, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        progress_callback()

    ###################################################################################

    DelBin = 'C:\\$Recycle.Bin'
    for filename in os.listdir(DelBin):
        file_path = os.path.join(DelBin, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        progress_callback()

    ###################################################################################

    DelLogs = 'C:\\Windows\\Logs'
    for filename in os.listdir(DelLogs):
        file_path = os.path.join(DelLogs, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
        progress_callback()

    ###################################################################################

    subprocess.run(['cleanmgr', '/sagerun:1'], shell=True)
    subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\DWM', '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)
    subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search', '/v', 'CortanaConsent', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)
    subprocess.run(['reg', 'add', 'HKCU\\Control Panel\\Desktop', '/v', 'WindowAnimation', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)

    registry_settings = [
        ('HKCU\\Control Panel\\Desktop', 'MenuShowDelay', 'REG_SZ', '0'),
        ('HKCU\\Control Panel\\Desktop', 'WindowAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'ComboBoxAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'SmoothScroll', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'CursorShadow', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'MenuFade', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'SelectionFade', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'ToolTipAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop', 'ToolTipFade', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'IconsOnly', 'REG_DWORD', '1'),
        ('HKCU\\Software\\Microsoft\\Windows\\DWM', 'EnableAeroPeek', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'TaskbarAnimations', 'REG_DWORD', '0'),
        ('HKCU\\Control Panel\\Desktop\\WindowMetrics', 'MinAnimate', 'REG_SZ', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'MenuAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'ToolTipAnimation', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 'ListviewAlphaSelect', 'REG_DWORD', '0'),
        ('HKCU\\Software\\Microsoft\\Windows\\DWM', 'EnableWindowShadow', 'REG_DWORD', '0')
    ]

    for key, value_name, value_type, value_data in registry_settings:
        subprocess.run(['reg', 'add', key, '/v', value_name, '/t', value_type, '/d', value_data, '/f'], shell=True)

    notification.notify(
        title='Cleanup Complete',
        message='Your computer is clean now, have a great day. --Emi',
        timeout=10
    )

###################################################################################

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.title = "Emi's Cleaner"
        self.icon = 'Rake.ico'
        with layout.canvas.before:
            Color(0x12/255, 0x07/255, 0x20/255, 1)
            self.rect = Rectangle(size=(layout.width, layout.height), pos=layout.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)

        self.label = Label(text="Click the button to clean your system", font_size=32, color=(1, 1, 1, 1))
        layout.add_widget(self.label)

        button = Button(
            text="Run Cleanup Script",
            size_hint=(None, None),
            size=(140, 50), padding=(10, 1),
            background_color=(0.945, 0.769, 0.059, 1.0)
        )
        button.bind(on_press=self.on_click)
        layout.add_widget(button)

        # "My Site" button
        my_site_button = Button(
            text="My Site",
            size_hint=(None, None),
            size=(75, 50), padding=(10, 1),
            background_color=(0.945, 0.769, 0.059, 1.0)
        )
        my_site_button.bind(on_press=self.open_site)
        layout.add_widget(my_site_button)

        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_click(self, instance):
        self.label.text = "Cleaning in progress..."
        run_cleanup_script(lambda: None) 
        self.label.text = "Your computer is clean now, have a great day. --Emi,"
    
    def open_site(self, instance):
        webbrowser.open("http://codescribe.tilda.ws")  

if __name__ == "__main__":
    # Install Python first if necessary
    check_and_install_python()

    # After Python installation completes, run the Kivy app
    MyApp().run()

###################################################################################
