import os
import numpy as np
import librosa
from tensorflow.keras.models import load_model
import speech_recognition as sr
import asyncio
import websockets
import tempfile

# Load pre-trained emotion detection model (CNN + LSTM)
model_path = os.path.expanduser('~/PycharmProjects/Emo-speech-training/emotion_model.keras')

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file '{model_path}' not found.")

model = load_model(model_path)


# Function to recognize speech and return audio
def capture_audio():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening for speech...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source)
            return audio
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for speech.")
            return None
        except Exception as e:
            print(f"Error capturing audio: {e}")
            return None


# Function to save recognized audio to a temporary file
def save_audio(audio):
    if audio is None:
        return None
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        with open(temp_audio_file.name, "wb") as f:
            f.write(audio.get_wav_data())
        return temp_audio_file.name


# Function to extract MFCC features from the audio signal
def extract_audio_features(audio_path):
    try:
        y, sr = librosa.load(audio_path, sr=22050)
    except Exception as e:
        print(f"Error loading audio file {audio_path}: {e}")
        return None

    # Extract only MFCCs to match the input of the trained model
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)

    # Pad or truncate to ensure consistent time steps (e.g., 130)
    fixed_length = 130
    if mfccs.shape[1] > fixed_length:
        mfccs = mfccs[:, :fixed_length]
    elif mfccs.shape[1] < fixed_length:
        padding = fixed_length - mfccs.shape[1]
        mfccs = np.pad(mfccs, ((0, 0), (0, padding)), mode='constant')

    return np.expand_dims(mfccs.T, axis=0)


# Classify emotion based on extracted features
def detect_emotion(audio_path):
    features = extract_audio_features(audio_path)
    if features is None:
        return "Error in feature extraction"

    # Reshape to match the expected input for the model (batch_size, time_steps, features)
    prediction = model.predict(features)

    emotion_labels = ["happiness", "sadness", "fear", "anger"]
    confidence = np.max(prediction)

    if confidence > 0.6:
        return emotion_labels[np.argmax(prediction)]
    else:
        return "uncertain"


# Real-time communication with WebSocket server
async def send_emotion_to_server(emotion):
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(emotion)
            response = await websocket.recv()
            print(f"Server response: {response}")
    except websockets.ConnectionClosed as e:
        print(f"Connection to server failed: {e}")
    except Exception as e:
        print(f"Error during WebSocket communication: {e}")


# Main function to handle the entire flow
def run_emotion_recognition():
    print("Starting Emo-Speech AI Robot...")

    # Capture and process audio
    audio = capture_audio()
    if audio is None:
        print("Speech recognition failed. Exiting.")
        return

    audio_path = save_audio(audio)
    if audio_path is None:
        print("Failed to save audio. Exiting.")
        return

    # Detect emotion from the audio
    emotion = detect_emotion(audio_path)
    print(f"Detected Emotion: {emotion}")

    # Send detected emotion to the server
    asyncio.run(send_emotion_to_server(emotion))


if __name__ == "__main__":
    run_emotion_recognition()
