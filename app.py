import logging
import sqlite3
from threading import Thread
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
import pyttsx3

# Load environment variables from .env file
load_dotenv()

from background_listener import start_background_listening
from emergency_module import SAFE_WORD, trigger_emergency
from voice_input import listen
from model import get_ai_response

# ------------------------------------
# App Setup
# ------------------------------------

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# Offline Text-to-Speech
engine = pyttsx3.init()

# ------------------------------------
# Voice Functions
# ------------------------------------

def speak(text: str):
    engine.say(text)
    engine.runAndWait()


def speak_async(text: str):
    Thread(target=speak, args=(text,)).start()

#ai response
def get_ai_response(message: str):

    normalized = message.strip().lower()

    if not normalized:
        return "Please say something so I can help you."

    # Special response for order
    if "order" in normalized:
        return "Your order is on the way."

    if "time" in normalized:
        from datetime import datetime
        return f"It is {datetime.now().strftime('%I:%M %p')} now."

    if "date" in normalized:
        from datetime import date
        return f"Today is {date.today():%B %d, %Y}."

    try:
        return get_ai_response(normalized)

    except Exception:
        return "I didn't understand that."


# ------------------------------------
# Database
# ------------------------------------

def save_chat(user, bot):

    conn = sqlite3.connect("chat_history.db")

    c = conn.cursor()

    c.execute(
        """CREATE TABLE IF NOT EXISTS chats(
        user TEXT,
        bot TEXT
        )"""
    )

    c.execute(
        "INSERT INTO chats VALUES (?,?)",
        (user, bot)
    )

    conn.commit()

    conn.close()

# ------------------------------------
# Routes
# ------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    message = data.get("message", "")

    location = data.get("location",  "LOCATION_NOT_AVAILABLE")

    # Emergency detection
    if SAFE_WORD.lower() in message.lower():

        trigger_emergency(location)

        reply = "Your order is on the way."

    else:

        reply = get_ai_response(message)

    speak_async(reply)

    save_chat(message, reply)

    return jsonify({"reply": reply})


@app.route("/voice")
def voice():

    text = listen()

    if SAFE_WORD.lower() in text.lower():

        trigger_emergency( "LOCATION_NOT_AVAILABLE")

        reply = "Your order will arrive soon."

    else:

        reply = get_ai_response(text)

    speak_async(reply)

    save_chat(text, reply)

    return jsonify({
        "reply": reply,
        "user": text
    })

# ------------------------------------
# Run App
# ------------------------------------

if __name__ == "__main__":

    # Start background emergency listener
    Thread(
        target=start_background_listening,
        daemon=True
    ).start()

    app.run(debug=True)