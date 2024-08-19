import platform
import subprocess
import os

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    if platform.system() == "Windows":
    
        command = [
            "pyinstaller",
            "console.py",
            "--onefile",
            f"--name=TOTK Console",
        ]
    elif platform.system() == "Linux":
        command = [
            "pyinstaller",
            "console.py",
            "--onefile",
            f"--name=TOTK Console.AppImage",
        ]

    subprocess.run(command, shell=True)