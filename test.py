import shutil, os, webbrowser, subprocess, time, ctypes, urllib.request
from plyer import notification
import tkinter as tk
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock  # To create the countdown with Kivy

# Define the functions based on your script
import shutil, os, webbrowser, subprocess, winreg, tkinter as tk, time, ctypes, urllib.request

###################################################################################
def Codescribe():
    webbrowser.open("http://codescribe.tilda.ws")

Codescribe()


###################################################################################

def run_cleanup_script():
    
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

    DelLogs = 'C:\Windows\Logs' 
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

    subprocess.run(['cleanmgr', '/sagerun:1'], shell=True)

    subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\DWM', '/v', 'EnableTransparency', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)

    subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search', '/v', 'CortanaConsent', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)

    subprocess.run(['reg', 'add', 'HKCU\\Control Panel\\Desktop', '/v', 'WindowAnimation', '/t', 'REG_DWORD', '/d', '0', '/f'], shell=True)



class MyApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10, )
        
        
        
        self.label = Label(text="Click the button to clean your system", font_size=32, color=(1, 1, 1, 1))
        layout.add_widget(self.label)

       
        button = Button(text="Run Cleanup Script", size_hint=(None, None), size=(200, 100))

       
        button.bind(on_press=self.on_click)

        layout.add_widget(button)

        return layout

    def on_click(self, instance):
        
        self.label.text = "Running the script..."

        
        run_cleanup_script()

       
        self.start_countdown()

    def start_countdown(self):
       
        self.label.text = "Self destructing in..."
     
        Clock.schedule_once(self.start_countdown_2, 3)

    def start_countdown_2(self, dt):
       
        self.label.text = "3"
        
        Clock.schedule_once(self.update_countdown_2, 1)

    def update_countdown_2(self, dt):
        
        self.label.text = "2"
       
        Clock.schedule_once(self.update_countdown_3, 1)

    def update_countdown_3(self, dt):
    
        self.label.text = "1"
        
        Clock.schedule_once(self.final_message, 2)

    def final_message(self, dt):
        
        self.label.text = "Jk"
        Clock.schedule_once(self.Greatday, 2)

    def Greatday(self, dt):
        
        self.label.text = "Your computer is clean now, have a great day. --Emi"



if __name__ == "__main__":
    MyApp().run()
