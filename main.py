import datetime
import os
import pprint
import random
import re
import sys
import time
import pyautogui
import pyjokes
import pywhatkit
import requests
import wolframalpha
from PIL import Image
from PyQt5.QtWidgets import *
from pywhatkit.exceptions import InternetException
from Jarvis import JarvisAssistant
from Jarvis.config import config
from Jarvis.features import Friday_Blueprint
from Jarvis.features.bot import *
from Jarvis.features import bot_voice

obj = JarvisAssistant()


# ================================ MEMORY ===========================================================================================================#


GREETINGS = ["hello jarvis", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

EMAIL_DIC = {
    'myself': 'faizeraza7720002@gmail.com',
    'my official email': "faizeraza4us@gmail.com",
    'Muhammad': 'muhammadsaad.sm2001@gmail.com',
    'vaishnavi': 'vaishnavinawalkar57@gmail.com',
    'kashif': 'kashifashhar9@gmail.com',
    'shruti': 'shrutirakhonde12@gmail.com',
    'achal' : 'ayushchavan3344@gmail.com'
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]

app_id = config.wolframalpha_id


# =======================================================================================================================================================


def speak(text):
    obj.tts(text)


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except Exception as e:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None


def startup():
    speak("Initializing Jarvis")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All systems have been activated")


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")
    elif 12 < hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")


class Sub_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.hi = bot_voice.Ui_Form()
        self.hi.setupUi(self)

    def __del__(self):
        sys.stdout = sys.__stdout__


class MainThread(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Friday_Blueprint.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_15.clicked.connect(self.TaskExecution)
        self.ui.pushButton_11.clicked.connect(self.bot_window)
        self.ui.pushButton_9.clicked.connect(self.usr_win)


    def __del__(self):
        sys.stdout = sys.__stdout__

    def usr_win(self):
        speak("This Feature is not available yet")

    def bot_window(self):
        self.jar = Sub_Window()
        self.jar.show()
        speak("After Making Change I Recommand you to restart Me")

    def TaskExecution(self):
        self.ui.label_2.setText("Listening...")
        if True:
            self.ui.label_2.setText("Thinking...")
            command = obj.mic_input()
            self.ui.textEdit.append("you:" + command)

            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                self.ui.textEdit.append("jarvis:" + date)
                speak(date)
            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                self.ui.textEdit.append("jarvis:" + f"Sir the time is {time_c}")
                speak(f"Sir the time is {time_c}")

            elif re.search('launch', command):
                dict_app = {
                    'chrome': 'C:/Program Files/Google/Chrome/Application/chrome',
                    'firefox': "C:/Program Files (x86)/Mozilla Firefox/firefox"
                }

                app = command.split(' ', 1)[1]
                path = dict_app.get(app)

                if path is None:
                    self.ui.textEdit.append('jarvis:' + 'Application path not found')
                    speak('Application path not found')
                    print('Application path not found')

                else:
                    self.ui.textEdit.append('jarvis:' + 'Launching: ' + app + 'for you sir!')
                    speak('Launching: ' + app + 'for you sir!')
                    obj.launch_any_app(path_of_app=path)

            elif command in GREETINGS:
                self.ui.textEdit.append(random.choice(GREETINGS_RES))
                speak(random.choice(GREETINGS_RES))

            elif re.search('open', command):
                domain = command.split(' ')[-1]
                open_result = obj.website_opener(domain)
                self.ui.textEdit.append(f'Alright sir !! Opening {domain}')
                speak(f'Alright sir !! Opening {domain}')
                print(open_result)

            elif 'weather' in command:
                try:
                    city = command.split('weather', 1)[1]
                    print(city)
                    weather_res = obj.weather(city=city)
                    print(weather_res)
                    self.ui.textEdit.append(weather_res)
                    speak(weather_res)
                except:
                    self.TaskExecution()

            elif re.search('tell me about', command):
                try:
                    topic = command.split(' ')[-1]
                    if topic:
                        wiki_res = obj.tell_me(topic)
                        print(wiki_res)
                        self.ui.textEdit.append(wiki_res)
                        speak(wiki_res)
                    else:
                        self.ui.textEdit.append("Sorry sir. I couldn't load your query from my database. Please try again")
                        speak(
                            "Sorry sir. I couldn't load your query from my database. Please try again")
                except:
                    self.ui.textEdit.append("Please try again")
                    speak("Pleas say again")
                    self.TaskExecution()
            elif "buzzing" in command or "news" in command or "headlines" in command:
                news_res = obj.news()
                self.ui.textEdit.append("jarvis: "+"Source: The Times Of India")
                speak('Source: The Times Of India')
                self.ui.textEdit.append("jarvis: "+"Todays Headlines are..")
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    pprint.pprint(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res) - 2:
                        break
                self.ui.textEdit.append("jarvis: "+"These were the top headline, Have a nice day Sir!!..")
                speak('These were the top headlines, Have a nice day Sir!!..')

            elif 'google for' in command:
                try:
                    obj.search_anything_google(command)
                except:
                    self.ui.textEdit.append("Please try again")
                    speak("Please try again")
                    self.TaskExecution()

            elif "music" in command or "music" in command:
                try:
                    music_dir = "D:\\MFR playlist"
                    songs = os.listdir(music_dir)
                    if "play" in command:
                        os.startfile(os.path.join(music_dir, songs[0]))

                    elif "stop" in command:
                        os.system("taskkill /f /im kmplayer.exe")
                    elif "next" in command:
                        cnt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
                        os.startfile(os.path.join(music_dir, songs[random.choice(cnt)]))
                except:
                    speak("Pleas Try Again")
                    self.TaskExecution()
            elif 'youtube' in command:
                try:
                    video = command.split(' ')[1]

                    speak(f"Okay sir, playing {video} on youtube")
                    self.ui.textEdit.append("jarvis: "+f"Okay sir, playing {video} on youtube")
                    pywhatkit.playonyt(video)
                except InternetException:
                    speak("sorry internet and i are not connected right now")
                    self.ui.textEdit.append("jarvis: "+"sorry internet and i are not connected right now")
                    self.TaskExecution()

            elif "email" in command or "send email" in command:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    speak("Whom do you want to email sir ?")
                    self.ui.textEdit.append("jarvis: "+"whom do you want to email sir ?")
                    recipient = obj.mic_input()
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:

                        speak("What is the subject sir ?")
                        self.ui.textEdit.append("jarvis: "+"What is the subject sir ?")
                        subject = obj.mic_input()
                        speak("What should I say?")
                        self.ui.textEdit.append("jarvis: "+"What should I say?")
                        message = obj.mic_input()
                        msg = 'Subject: {}\n\n{}'.format(subject, message)
                        obj.send_mail(sender_email, sender_password,
                                      receiver_email, msg)
                        speak("Email has been successfully sent")
                        self.ui.textEdit.append("jarvis: "+"Email has been successfully sent")
                        time.sleep(2)

                    else:
                        speak(
                            "I couldn't find the requested person's email in my database. Please try again with a "
                            "different name")
                        self.ui.textEdit.append("jarvis: "+"I couldn't find the requested person's email in my database. Please try again with a "
                            "different name")

                except:
                    speak("Sorry sir. Couldn't send your mail. Please try again")
                    self.ui.textEdit.append("jarvis: "+"Sorry sir. Couldn't send your mail. Please try again")
                    self.TaskExecution()

            elif "calculate" in command:
                try:
                    question = command
                    answer = computational_intelligence(question)
                    speak(answer)
                    self.ui.textEdit.append("jarvis: "+answer)

                except:
                    self.TaskExecution()
            elif "what is" in command :
                try:
                    question = command
                    answer = computational_intelligence(question)
                    speak(answer)
                    self.ui.textEdit.append("jarvis: "+answer)
                except:
                    speak("sorry sir i dont know about that")
                    self.TaskExecution()

            elif "make a note" in command or "write this down" in command or "remember this" in command:
                try:
                    speak("What would you like me to write down?")
                    self.ui.textEdit.append("jarvis: "+"What would you like me to write down?")
                    note_text = obj.mic_input()
                    obj.take_note(note_text)
                    speak("I've made a note of that")
                    self.ui.textEdit.append("jarvis: "+"I've made a note of that")
                except Exception as e:
                    print(e)
                    speak("unable to make note")
                    self.ui.textEdit.append("jarvis: "+"unable to make note")
            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                self.ui.textEdit.append("jarvis: " + "Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)
                self.ui.textEdit.append("jarvis: "+joke)

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)
                self.ui.textEdit.append("jarvis: "+sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)
                        self.ui.textEdit.append("jarvis: "+res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)
                        self.ui.textEdit.append("jarvis: "+res)

                except Exception:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)
                    self.ui.textEdit.append("jarvis: "+res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")
                self.ui.textEdit.append("jarvis: "+f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                self.ui.textEdit.append("jarvis: "+"Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                # noinspection PyBroadException
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(f"You are currently in {city} city which is in {state} state and country {country}")
                    self.ui.textEdit.append("jarvis: "+f"you are currently in {city} city which is in {state}")
                except Exception:
                    speak(
                        "Sorry sir, I could not fetch your current location. Please try again")
                    self.ui.textEdit.append("jarvis: "+"Sorry sir, I could not fetch your current location. Please try again")

            elif "take screenshot" in command:
                speak("By what name do you want to save the screenshot?")
                self.ui.textEdit.append("jarvis: "+"By what name do you want to save the screenshot")
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                self.ui.textEdit.append("jarvis: "+"Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                img.save(name + ".png")
                speak("The screenshot has been successfully captured")
                self.ui.textEdit.append("jarvis: "+"The screenshot has been successfully captured")

            elif "show screenshot" in command:
                try:
                    speak("which one sir")
                    self.ui.textEdit.append("jarvis: "+"which one sir")

                    name = obj.mic_input()
                    img = Image.open("D:\\jarvis\\" + name + ".png")
                    img.show(img)
                    speak("Here it is sir")
                    self.ui.textEdit.append("jarvis: "+"Here it is sir")
                except Exception:
                    speak("Sorry sir, I am unable to display the screenshot")
                    self.ui.textEdit.append("jarvis: "+"I ma unable to display the screenshot")

            elif "hide all files" in command or "hide this folder" in command:
                os.system("attrib +h /s /d")
                speak("Sir, all the files in this folder are now hidden")
                self.ui.textEdit.append("jarvis: "+"Sir, all the files in this folder are now")
            elif "visible" in command or "make files visible" in command:
                os.system("attrib -h /s /d")
                speak(
                    "Sir, all the files in this folder are now visible to everyone. I hope you are taking this "
                    "decision in your own peace")
                self.ui.textEdit.append("jarvis: "+"Sir, all the files in this folder are now visible to everyone. I hope you are taking this "
                    "decision in your own peace")
            elif "how" in command or "why" in command:
                try:
                    query = command
                    answer = computational_intelligence(query)
                    speak(answer)
                    self.ui.textEdit.append("jarvis: "+answer)
                except Exception:
                    speak("sorry, sir i am not able to search that")
                    self.ui.textEdit.append("jarvis: "+"sorry, sir i am not able to search that")
                    self.TaskExecution()
            elif "sleep" in command or "stop hearing" in command:
                pass

            else:
                message = command
                ints = predict_class(message)
                res = get_response(ints, intents)
                print(res)
                speak(res)
                self.ui.textEdit.append("jarvis: "+res)
            self.ui.label_2.setText("waiting...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = MainThread()
    jarvis.show()
    startup()
    wish()
    exit(app.exec_())
