import queue
import json
import sounddevice as sd
from vosk import Model, KaldiRecognizer
from emergency_module import SAFE_WORD, trigger_emergency

# Load Vosk model (offline speech recognition)
model = Model("vosk_model")

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def start_background_listening():

    print("Background listener started...")

    rec = KaldiRecognizer(model, 16000)

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype='int16',
        channels=1,
        callback=callback
    ):

        while True:
            data = q.get()

            if rec.AcceptWaveform(data):

                result = json.loads(rec.Result())
                text = result.get("text", "")

                if text != "":
                    print("Heard:", text)

                # SAFE WORD DETECTION
                if SAFE_WORD.lower() in text.lower():

                    print("SAFE WORD DETECTED")

                    trigger_emergency("0,0")