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
python -m venv .venv
source .venv/bin/activate  # For Windows: .venv\Scripts\activate

pip install -r requirements.txt
