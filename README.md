
# Siri-Py-A-Simple-Python-Voice-Assistant

## 📌 Overview
The **Siri Virtual Assistant** is a Python-based voice-controlled AI assistant that can perform a variety of tasks such as answering questions, opening websites, playing music, giving the current time, and more.  
It uses **speech recognition** for voice commands, **text-to-speech** for responses, and integrates with popular libraries like Wikipedia and PyWhatKit for dynamic functionality.


## 🚀 Features
- 🎤 **Voice Command Recognition** – Listens to and processes user voice inputs.
- 🗣 **Text-to-Speech Responses** – Replies with a natural-sounding voice.
- 📚 **Wikipedia Search** – Retrieves quick summaries of topics.
- 🌐 **Web Browsing** – Opens websites like Google, YouTube, and online games.
- 🎶 **Music Playback** – Plays songs directly from YouTube.
- ⏰ **Time Updates** – Tells the current time.
- 💬 **Casual Conversations** – Responds to greetings and small talk.
- 🏥 **Basic Medical Information** – Retrieves health-related info from Wikipedia (not for diagnosis).
- ⏯ **Pause & Resume** – Ability to pause listening and resume later.
- 🔄 **Multi-command Support** – Recognizes a variety of natural speech patterns.


## 🛠 Technologies Used
- **Python 3**
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – For voice input processing
- [pyttsx3](https://pypi.org/project/pyttsx3/) – For text-to-speech
- [Wikipedia](https://pypi.org/project/wikipedia/) – To fetch quick summaries
- [webbrowser](https://docs.python.org/3/library/webbrowser.html) – To open URLs
- [PyWhatKit](https://pypi.org/project/pywhatkit/) – For YouTube song playback
- [datetime](https://docs.python.org/3/library/datetime.html) – For time-based responses

## 📂 Project Structure

## ⚙️ Installation & Setup
1. **Clone the repository**  
   git clone https://github.com/your-username/siri-virtual-assistant.git
   cd siri-virtual-assistant

2.**Install dependencies**
pip install speechrecognition pyttsx3 wikipedia pywhatkit

3.**Run the assistant**
python ai.py

## 🎯 Example Commands
- **"Wikipedia Albert Einstein"** → Reads a short summary from Wikipedia.
- **"Open YouTube"** → Opens YouTube in your browser.
- **"Play Shape of You"** → Plays the song on YouTube.
- **"Time"** → Tells the current time.
- **"Pause"** → Pauses listening.
- **"Resume"** → Resumes listening.
