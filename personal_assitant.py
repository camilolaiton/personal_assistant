import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import subprocess

# sudo apt install libespeak1 ||| for fixing bug in linux

browser = None
browsers = ("firefox", "chromium", None)

class personal_assistant():

    def __init__(self, name):
        self.voice_engine = pyttsx3.init()
        self.name = name
        self.working = True
        self.browser = wb.get(browsers[0])

        """
            Configuring assistant's voice
        """

        self.voice_engine.setProperty('rate', 150)
        self.voice_engine.setProperty('voice', 'english-us')

        self.starting_assistant()

    def assistant_speaks(self, msg):
        self.voice_engine.say(msg)
        self.voice_engine.runAndWait()
    
    def starting_assistant(self):
        hour = datetime.datetime.now().hour
        time_message = 'Good afternoon'

        if (hour >= 6 and hour <= 12):
            time_message = 'Good morning'
        elif (hour >= 18):
            time_message = 'Good night'

        self.assistant_speaks(time_message + " sir, I am " + self.name + ", your personal assistant. How can I help you?")

    def assistant_says_time(self):
        time = datetime.datetime.now().strftime("%I hours, %M minutes and %S seconds")
        self.assistant_speaks(time)
    
    def assitant_says_date(self):
        date = datetime.datetime.now().strftime("%A %d %B of %Y")
        self.assistant_speaks(date)

    def get_command(self):
        r = sr.Recognizer()
        command = None

        while (True):
            with sr.Microphone() as source_info:
                print("[+] Listening...")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source_info, duration = 0.5)
                audio = r.listen(source_info)

            try:
                print("[+] Recognizing...")
                command = r.recognize_google(audio, language="en-US")
                print("[+] Listened command: ", command)
                break

            except Exception as err:
                print(err)
                self.assistant_speaks("Could you please say that again?")
        
        return command.lower()

    def open_browser(self):
        self.assistant_speaks("Where should I open it?")
        page = self.get_command()
        self.assistant_speaks("Openning in ".format(browsers[0]))
        self.browser.open(page, new=0, autoraise=True)

    def shell_intruction(self):
        self.assistant_speaks("What do you want to execute?")
        shell_command = self.get_command()
        print(shell_command)
        self.assistant_speaks("Executing in command in shell")

        try:
            out = subprocess.run(shell_command.split(' '))
            self.assistant_speaks("Showing results in actual shell")
            print("out: ", out)
    
        except Exception:
            self.assistant_speaks("Sir, there's an error with your command. Try again.")

    def run(self):

        while(self.working):

            command = self.get_command()

            if self.name in command:
                self.assistant_speaks('Yes, sir')

            if 'time' in command:
                self.assistant_says_time()
            elif 'date' in command:
                self.assitant_says_date()
            elif 'browser' in command:
                self.open_browser()
            elif 'offline' in command:
                self.assistant_speaks("Going offline...")
                self.working = False
            elif 'shell' in command:
                self.shell_intruction()
            else:
                self.assistant_speaks("I can't recognize this command!")

def main():
    personal1 = personal_assistant("raphael")   # Rapha-L
    # personal1.get_command()
    personal1.run()
    # personal1.assistant_says_time()
    # personal1.assitant_says_date()

if __name__ == "__main__":
    main()

"""
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
"""
