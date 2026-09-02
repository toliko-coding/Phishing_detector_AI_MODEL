# SMSNet — AI-Powered Phishing Detection

SMSNet is a browser-based tool that detects phishing attempts in SMS messages using a machine learning model trained on labeled message data. It runs entirely client-side with TensorFlow.js, analyzing pasted messages in real time and improving over time from user feedback.

## Features

- **AI-Powered Detection** — classifies SMS content as phishing or safe using a model trained on real message data.
- **Real-Time Analysis** — evaluates messages instantly in the browser, no server round-trip required for inference.
- **Feedback Loop** — users can report misclassifications, which are stored in Firebase for future retraining.
- **Educational Resources** — an About page explains phishing tactics and safety tips.
- **Responsive UI** — Bootstrap-based interface that works across devices.

## How It Works

1. **Paste a message** — the user pastes a suspicious SMS into the app.
2. **Model inference** — a TensorFlow.js model, loaded in the browser, predicts the likelihood of phishing.
3. **Feedback** — users can flag incorrect predictions; reports are sent to Firebase Realtime Database.
4. **Retraining** — the Python scripts in `public/model/` pull the collected reports, preprocess them, and retrain the model.

## Technology Stack

- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Machine Learning (inference):** TensorFlow.js, PapaParse
- **Machine Learning (training):** Python, TensorFlow/Keras, scikit-learn, pandas, tensorflowjs
- **Data Store:** Firebase Realtime Database
- **Hosting:** Firebase Hosting

## Project Structure

```
public/
  index.html            # Main app UI
  about.html             # Educational content
  css/, js/, images/     # Static assets
  trainmodel.js          # Client-side model training/inference helper
  model/
    fetch_and_preprocess_data.py   # Pulls & cleans data from Firebase
    train_model.py                 # Trains the classifier and exports to TF.js format
    convert_model.py               # Model conversion utility
    preprocessed_data.csv/.json    # Training data
    word_index.json                # Tokenizer vocabulary
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/toliko-coding/Phishing_detector_AI_MODEL.git
   cd Phishing_detector_AI_MODEL
   ```

2. Install JS dependencies (Firebase SDK):
   ```bash
   npm install
   ```

3. (Optional) Retrain the model:
   ```bash
   python3 public/model/fetch_and_preprocess_data.py
   python3 public/model/train_model.py
   ```
   This fetches labeled reports from Firebase, preprocesses them, and trains a new model.

4. Serve `public/` locally (e.g. `npx serve public` or open `public/index.html` directly), or deploy with:
   ```bash
   firebase deploy
   ```

## Description

SMSNet is an AI-driven web app that detects SMS phishing using a TensorFlow.js model trained on labeled data and run directly in the browser. Paste a message to get an instant risk score, then submit feedback to Firebase to help retrain the model. It pairs real-time detection with phishing-awareness education in a responsive interface.
