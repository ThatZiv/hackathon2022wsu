import os
import subprocess
import keyboard

class Constants:
    class path:
        server1 = "\"\\\\server1.zavaar.net\""
        server0 = "\"\\\\admin.zavaar.net\""
        school = "Z:\\Documents\\College"
        user = "C:\\Users\\Zavaar"
        chrome = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        z = "C:\\z" # Zua CLI Root
    class ws:
        path = "\\Desktop\\testing\\pyarduino\\ws_client"

class Keys:
    def switch(key, val):  # actions
        # really poop way of switch case logic 
        # NOTES:
        #   I could've binded them to a dict
        #   and called them whenever to get constant runtime
        #   AND USED THE ACTUAL ID NUMBER,
        #   but I didn't really want to and also had minimal time :(
        #   However, since the maximun number of keys are 128,
        #   one can assume that the runtime can never be too bad
        if key == "C4":
            os.system(f"start explorer.exe {Constants.path.server1}")
        elif key == "D4":
            os.system(f"start explorer.exe {Constants.path.server0}")
        elif key == "E4":
            os.system(f"start explorer.exe {Constants.path.school}")
        elif key == "C#4":
            subprocess.Popen(
                [Constants.path.chrome], shell=False)
        elif key == "D#4":
            subprocess.Popen(
                [Constants.path.chrome, "-incognito"], shell=False)
        elif key == "F4":
            os.system(f"start notepad {Constants.path.school}\\agenda.txt")
        elif key == "G4":
            os.system("start notepad")
        elif key == "D#6":
            subprocess.Popen([
                Constants.path.user + Constants.ws.path + "\\chUp.exe"
            ], shell=False)
        elif key == "C#6":
            subprocess.Popen([
                Constants.path.user + Constants.ws.path + "\\chDown.exe"
            ], shell=False)
        elif key == "C5":
            keyboard.media_prev()
        elif key == "D5":
            keyboard.media_play_pause()
        elif key == "E5":
            keyboard.media_next()
        elif key == "C#5":
            keyboard.volume_down(val)
        elif key == "D#5":
            keyboard.volume_up(val)
        elif key == "F5":
            keyboard.a_key() # mute discord
        elif key == "G5":
            keyboard.b_key() # deafen discord
        elif key == "E6":
            subprocess.Popen([
                "cmd", "/c", "C:\\z\\z", "scr" # Zua CLI integration
            ], cwd="C:\\Windows\\System32", shell=False)
            #os.system("cmd /k C:\\z\\z scr")
            #os.system("cmd /c C:\Windows\System32\Ribbons.scr -start") 
        elif key == "F#6":
            os.system("start sndvol.exe")
        #extra stuff BELOW
        elif key == "C3":
            os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ") # 😳
        elif key == "D3":
            os.system("start https://zavaar.net")
        elif key == "E3":
            os.system("start https://wayne.edu")
            

