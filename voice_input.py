import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

# Load model once
model = Model("vosk_model")

def listen(duration=5):
    q = queue.Queue()  # Create a fresh queue for each listen
    def callback(indata, frames, time, status):
        if status:
            print(status)
        q.put(bytes(indata))

    rec = KaldiRecognizer(model, 16000)
    text = ""

    try:
        with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                               channels=1, callback=callback):
            print("🎙 Listening...")
            for _ in range(int(duration * 16000 / 8000)):
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = json.loads(rec.Result())
                    text = result.get("text", "")
    except Exception as e:
        print("Error accessing microphone:", e)

    print("Recognized:", text)
    return text