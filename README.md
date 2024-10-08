Emo-Voice-AI

Emo-Voice-AI: is an AI-driven speech-to-emotion recognition system. It captures audio in real-time, processes the speech using a pre-trained CNN + LSTM model, detects the emotion, and sends the result to a WebSocket server. This project leverages Python libraries such as TensorFlow, Librosa, SpeechRecognition, and WebSockets for real-time emotion recognition and communication.

Features

- Captures real-time audio input from the microphone.
- Extracts audio features (MFCC) for emotion recognition.
- Utilizes a pre-trained CNN + LSTM model to classify emotions.
- Supports emotions such as happiness, sadness, fear, and anger.
- Sends detected emotion via WebSocket to a server.

Project Structure

- `emo_voice_ai.py`: Main script that handles audio capture, emotion detection, and communication with the WebSocket server.
- `websocket_server.py`: Script for the WebSocket server that receives and echoes emotion data.
- `.github/workflows/`: Contains GitHub Actions workflow for linting and testing.
- `.pylintrc`: Pylint configuration file.
- `.gitignore`: Specifies files and directories to be ignored in Git version control.

Technologies Used

- Python: The main programming language for the project.
- TensorFlow: Used to load and run the pre-trained CNN + LSTM model for emotion detection.
- Librosa: For audio processing and feature extraction (MFCC).
- SpeechRecognition: For capturing real-time audio input from the microphone.
- WebSockets: For real-time communication between the emotion recognition system and the WebSocket server.

Setup Instructions

To set up and run the Emo-Voice-AI project on your local machine, follow these steps:

1. Clone the Repository

```bash
git clone https://github.com/mo-elamin/Emo-Voice-AI.git
cd Emo-Voice-AI
```

2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate
```

3. Install Dependencies

Install all required Python libraries:

```bash
pip install -r requirements.txt
```
4. Train or Use Pre-trained Model

The project assumes that you have a pre-trained emotion detection model stored at: ~/PycharmProjects/Emo-speech-training/emotion_model.keras. If you do not have this model, you will need to train one separately or acquire an emotion recognition model.

5. Run the WebSocket Server

First, start the WebSocket server that will receive emotion data:

```bash
python websocket_server.py
```
You should see the following message:
```bash
WebSocket server started on ws://localhost:8765
```
6. Run the Emotion Recognition Script

With the WebSocket server running, start the emotion recognition script:
```bash
python emo_voice_ai.py
```
This will capture real-time audio, process it, detect emotions, and send the results to the WebSocket server.


