import subprocess
import datetime


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    notepad = r"C:\Windows\System32"
    subprocess.Popen([notepad, file_name])

