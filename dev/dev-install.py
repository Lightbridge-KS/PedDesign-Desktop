# Run This Script from Project Root (Dev Only)
import os
import subprocess
from sys import platform
from pathlib import Path

# Step 1: Give App Name & Icon Path
app_name = "PedDesignCT"
app_icon_path = "assets/PedDesignCT.ico"

print(os.getcwd()) # Project root

home_dir = str(Path.home()) # User Home Directory

def get_pkg_path(pkg, system):
    # Step 2: Provide Path to `site-packages`
    path_mac = "/Users/kittipos/.pyenv/versions/3.11.0/lib/python3.11/site-packages/"
    path_win = "C:\\Users\\prach\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\"
    if system == "mac":
        return f"{path_mac}{pkg}:{pkg}/"
    if system == "win":
        return f"{path_win}{pkg};{pkg}/"

# Run
if platform == "darwin":
    print("On Mac")
    # Run on Mac
    cmd_mac_str = f"""
pyinstaller --noconfirm --onedir -n '{app_name}' --windowed --add-data '{get_pkg_path("customtkinter", "mac")}' --icon='{app_icon_path}' app.py
cd dist
tar -czf {app_name}-macos.tar.gz {app_name}.app
"""
    subprocess.run(cmd_mac_str, shell=True)
    # print(cmd_mac_str)
else:
    print("On Windows")
    # Run on Win
    cmd_win_str = fr"""
pyinstaller --noconfirm --onefile -n {app_name} --windowed --add-data '{get_pkg_path("customtkinter", "win")}' --icon='{app_icon_path}' app.py
""" 
    # os.system(cmd_win_str)
    # Zip File
    # os.chdir("dist") 
    # os.system(f"powershell -Command Compress-Archive -Path {app_name}.exe -DestinationPath {app_name}-win.zip")
    print(cmd_win_str)
    #subprocess.run(cmd_win_str, shell=True) # Not work