import subprocess
import os

# /screenshot
def screenshot():
    isExist = subprocess.run("ls ./screenshot.png", shell=True, capture_output=True, text=True)
    if isExist == './screenshot.png\n':
        os.system("rm -f './screenshot.png'")

    os.system("scrot screenshot.png")

    return "./screenshot.png"

# /updates


# reboot
