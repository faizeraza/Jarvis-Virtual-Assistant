import os
import pyautogui
import wikipedia
import smtplib


class taskWithOS():

    def screenshot(self):
        # save screenshot to picture folder
        save_path = os.path.join(os.path.expanduser("~"), "pictures")
        shot = pyautogui.screenshot()
        shot.save(f"{save_path}\\python_screenshot.png")
        return print(f"\nScreenshot taken,and saved to {save_path}")


class taskWithInternet():
    def sendEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('faizeraza4us@gmail.com', 'faizan754')
        server.sendmail('faizeraza4us@gmail.com', to, content)
        server.close()
