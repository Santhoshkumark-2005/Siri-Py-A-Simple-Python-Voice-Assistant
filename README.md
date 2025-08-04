# 🧠 Siri-Py: A Python-Powered Virtual Voice Assistant

Siri-Py is an intelligent, voice-activated virtual assistant developed in Python. Designed to understand natural speech and respond with synthesized voice output, it can execute a wide range of tasks including web navigation, media playback, time queries, and information retrieval via Wikipedia. This project showcases an integration of speech recognition, text-to-speech, and intelligent command handling to build an interactive, hands-free assistant experience.

---

## 🎯 Project Objective

To develop a modular, customizable voice assistant capable of understanding and executing basic spoken commands in English, with basic multilingual support. The project demonstrates real-time voice interaction, speech recognition, and audio response using Python libraries.

---

## 🔧 Core Features

- 🎙 **Speech Recognition:** Real-time command listening via microphone  
- 🗣 **Text-to-Speech:** Natural voice responses using `pyttsx3`  
- 🌐 **Wikipedia Integration:** Quick summaries for general knowledge queries  
- 📺 **YouTube Playback:** Play songs or videos via `pywhatkit`  
- 🕒 **Time Inquiry:** Announces the current time  
- 🧠 **Basic AI Responses:** Understands simple queries like greetings, gratitude, and identity  
- 🌍 **Web Automation:** Opens common websites like Google, YouTube, and online games  
- ⚕ **Medical Inquiry Placeholder:** Responds to medical topics using Wikipedia summaries  
- 🔄 **Session Management:** Pause and resume the assistant via voice command  

---

## 📦 Tech Stack

- **Python 3.x**
- [`speech_recognition`](https://pypi.org/project/SpeechRecognition/)
- [`pyttsx3`](https://pypi.org/project/pyttsx3/)
- [`wikipedia`](https://pypi.org/project/wikipedia/)
- [`pywhatkit`](https://pypi.org/project/pywhatkit/)
- `webbrowser` (standard library)
- `datetime` (standard library)

---

## 🚀 Getting Started

### Prerequisites

Ensure Python 3.x and `pip` are installed on your machine.

### Installation

```bash
git clone https://github.com/yourusername/siri-py.git
cd siri-py
pip install -r requirements.txt

pip install speechrecognition pyttsx3 wikipedia pywhatkit

Run the Assistant
python ai.py

