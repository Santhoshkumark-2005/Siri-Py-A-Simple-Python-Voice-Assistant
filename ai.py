import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pywhatkit

class SiriAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)

        # Set voice
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)  # Try female
        else:
            self.engine.setProperty('voice', voices[0].id)

        self.paused = False
        self.greet_user()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self):
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            self.speak("Good morning!")
        elif 12 <= hour < 18:
            self.speak("Good afternoon!")
        else:
            self.speak("Good evening!")

        self.speak("I am Siri, your virtual assistant. How can I assist you today?")

    def listen_command(self):
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                command = self.recognizer.recognize_google(audio)
                print("You said:", command)
                return command.lower()
        except sr.WaitTimeoutError:
            self.speak("Listening timed out. Please speak more quickly.")
        except sr.UnknownValueError:
            self.speak("Sorry, I didn't catch that.")
        except sr.RequestError:
            self.speak("Network error. Please check your internet connection.")
        except OSError:
            self.speak("Microphone not found or not working.")
        return ""

    def execute_command(self, command):
        if 'wikipedia' in command:
            self.speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                self.speak("According to Wikipedia")
                self.speak(result)
            except wikipedia.exceptions.PageError:
                self.speak("Sorry, I couldn't find any information on that topic.")
            except wikipedia.exceptions.DisambiguationError:
                self.speak("There are multiple results for this term. Please be more specific.")
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
        elif 'play games' in command:
            webbrowser.open("https://www.onlinegames.com")
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
        elif 'play music' in command or 'play' in command:
            song = command.replace("play music", "").replace("play", "").strip()
            self.speak(f"Playing {song} on YouTube...")
            pywhatkit.playonyt(song)
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            self.speak(f"The current time is {current_time}")
        elif 'thank you' in command:
            self.speak("You're welcome!")
        elif 'how are you' in command:
            self.speak("I'm doing well, thank you for asking!")
        elif 'know tamil' in command:
            self.speak("Enakku konjam konjam Tamil theriyum")
        elif 'your name' in command:
            self.speak("I am Siri, your personal assistant.")
        elif 'medical advice' in command:
            self.speak("I'm not a doctor. Please consult a medical professional.")
        elif 'medical condition' in command:
            self.speak("Please specify the medical condition you want to learn about.")
            condition = self.listen_command()
            self.speak("Searching for information about " + condition)
            try:
                result = wikipedia.summary(condition, sentences=2)
                self.speak(result)
            except wikipedia.exceptions.DisambiguationError:
                self.speak("There are multiple results for this term. Please be more specific.")
        elif 'emergency' in command:
            self.speak("If you're experiencing an emergency, please call emergency services immediately.")
        elif 'exit' in command:
            self.speak("Goodbye! Have a nice day.")
            exit()
        elif 'pause' in command:
            self.speak("Pausing. Say 'resume' to continue.")
            self.paused = True
        elif 'resume' in command:
            self.speak("Resuming.")
            self.paused = False
        else:
            self.speak("Sorry, I didn't understand that. Can you repeat?")

    def run(self):
        while True:
            if not self.paused:
                command = self.listen_command()
                if command:
                    self.execute_command(command)
            else:
                command = self.listen_command()
                if 'resume' in command:
                    self.execute_command(command)

if __name__ == "__main__":
    siri = SiriAssistant()
    siri.run()
