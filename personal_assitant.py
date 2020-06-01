import pyttsx3
import datetime
import speech_recognition as sr

# sudo apt install libespeak1 ||| for fixing bug in linux

class personal_assistant():

    def __init__(self, name):
        self.voice_engine = pyttsx3.init()
        self.name = name
        self.working = True

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
                r.adjust_for_ambient_noise(source_info, duration = 1)
                audio = r.listen(source_info)

            try:
                print("[+] Recognizing...")
                command = r.recognize_google(audio, language="en-US")
                print("[+] Listened command: ", command)
                break

            except Exception as err:
                print(err)
                self.assistant_speaks("Could you please say that again?")
        
        return command

    def run(self):

        while(self.working):

            command = self.get_command().lower()

            if self.name in command:
                self.assistant_speaks('Yes, sir')

            if 'time' in command:
                self.assistant_says_time()
            elif 'date' in command:
                self.assitant_says_date()
            elif 'offline' in command:
                self.working = False

def main():
    personal1 = personal_assistant("rafael")   # Rapha-L
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
