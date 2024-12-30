# Phishing_detector_AI_MODEL
SMSNet is an AI-powered phishing detection tool that protects users from malicious SMS messages. It analyzes messages in real time, identifying potential threats while learning from user feedback to improve accuracy. With live detection, educational resources, and a user-friendly interface, SMSNet ensures a safer messaging experience.

SMSNet: AI-Powered Phishing Detection App

SMSNet is an advanced phishing detection tool designed to protect users from malicious SMS messages. This app uses machine learning to analyze SMS content and determine whether it’s a phishing attempt. With real-time detection, user feedback integration, and educational resources, SMSNet ensures a safer messaging experience.

Features
	•	AI-Powered Detection: Detects phishing attempts using an AI model trained on SMS data.
	•	Real-Time Protection: Analyzes SMS messages as they arrive, flagging potential threats instantly.
	•	Interactive Learning: Continuously improves detection accuracy through user feedback.
	•	Educational Resources: Includes a page dedicated to educating users about phishing and staying safe.
	•	User-Friendly Design: Offers a sleek, responsive UI for a seamless user experience.

 How It Works
	1.	Analyze Messages: Users paste suspicious SMS messages into the app.
	2.	AI Model Evaluation: The app’s AI model predicts the likelihood of phishing.
	3.	Feedback Integration: Users can provide feedback to help the AI learn and improve.
	4.	Education: Users can access resources to learn more about phishing threats.

 Technology Stack
	•	Frontend: HTML, CSS, JavaScript, Bootstrap
	•	Machine Learning: TensorFlow.js
	•	Data Parsing: PapaParse.js
	•	Hosting: GitHub Pages
	•	Version Control: GitHub

 Setup Instructions
	1.	Clone the repository:
     git clone https://github.com/<your-username>/SMSNet.git
     cd SMSNet

	2.	Run the Machine Learning Model:
	•	Step 1: Fetch and preprocess data:
 python3 model/fetch_and_preprocess_data.py


 	Step 2: Train the model:

  python3 model/trainmodel.py

  These scripts will download SMS data from your database, preprocess it, and train a machine learning model. The trained model will then be saved and ready to integrate with the app.

	3.	Open the index.html file in a browser to start using SMSNet.
