# 🛡️ Guardian AI
### *Voice-Enabled Emergency Assistant*

Guardian AI is an AI-powered voice assistant designed to provide intelligent conversation and emergency safety support.
It allows users to interact using text or voice commands and can detect emergency situations using a predefined safe phrase.

The system runs completely offline AI using a local language model via Ollama, ensuring privacy, low latency, and zero API dependency..

---

## 📑 Table of Contents

- Features  
- Project Structure  
- Tech Stack  
- Setup Instructions  
- Demo
- Demo Vedio
- Offline Capability
- Author  
- License
- Contribution

---

## ✨ Features

 - AI chatbot with intelligent responses
 - Voice input using speech recognition
 - Voice output using text-to-speech
 - Emergency detection via safe phrase
 - Browser Geolocation API
 - SMS alert system  
 - Chat history storage
 - Web-based user interface
---

## 📁 Project Structure
```text
Guardian-AI
│
├── app.py
├── model.py
├── emergency_module.py
├── voice_input.py
├── background_listener.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── requirements.txt
└── README.md
```
---

## ⚙️ Tech Stack

### Frontend  
- HTML 
- CSS 
- JavaScript  

### Backend  
- Python 
- Flask
  
### AI / LLM
- Ollama
- Phi-3 Mini
  
### Voice Processing
- Vosk
- pyttsx3
  
### Communication
- Twilio (SMS Alerts)
  
### Database
- SQLite


---

## 🚀 Setup Instructions
```bash
   1️⃣ Clone the repository
    git clone https://github.com/yourusername/Guardian-AI.git
    cd Guardian-AI
    
    2️⃣ Install dependencies
    pip install -r requirements.txt
    
    3️⃣ Install Ollama
    Download and install Ollama.
    Then run:
    ollama pull phi3
    
    4️⃣ Open Browser
    http://127.0.0.1:5000
```
##  Demo 
### 💻 Text Interaction
- User types a message in chat
- AI responds instantly
### 🎤 Voice Interaction
- Click microphone
- Speak command
- AI replies with voice
### 🚨 Emergency Feature
Say: "order pizza"
System:
- Detects safe word
- Gets location
- Sends alert

## DEMO VEDIO
▶️ **Watch the demo here:**  
[Click to watch demo](https://drive.google.com/file/d/1JpW74Gqc4waX99YJCh7koe8BdD7Z0xHM/view?usp=drivesdk)

### sms recieved with location
[SMS](https://drive.google.com/file/d/1nemAAZr65fpbfBAt7hltH98-MiPWjwPS/view?usp=drivesdk)

## 🔒  Offline Capability 
- AI runs locally using Ollama
- Voice recognition works offline using Vosk
- Text-to-speech works offline using pyttsx3
- Emergency events are stored locally if network is unavailable

## 👩‍💻 Author 

Vidushi Gupta

## 📜 License 

This project is for educational and research purposes.

## ⭐ Contribution 

Feel free to fork the repository and contribute!
