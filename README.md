🛡️ Digital Armor – Scam Message Detector

Inspiration
Every day, thousands of people fall victim to online scams — fake job offers, phishing emails, and fraudulent messages. I wanted to create a tool that helps ordinary users detect scams instantly and safely browse digital platforms.

What it does
Digital Armor uses AI to analyze text messages, emails, or job alerts and predicts whether they are 🚨 Scam or ✅ Safe. It also shows a confidence score to help users make informed decisions.

How we built it

Frontend: Streamlit for a simple, interactive UI.

Backend AI: mrm8488/bert-tiny-finetuned-sms-spam-detection model via Hugging Face Inference API.

Extras: Fallback keyword detection for urgent or suspicious messages.

Deployment: Live on Streamlit sharing / Hugging Face Spaces.

Challenges we faced

Managing API response times to avoid timeouts.

Ensuring clear UX while providing accurate scam detection.

Accomplishments

Fully functional prototype analyzing messages in seconds.

Publicly accessible live demo.

Simple interface that’s easy for any user to test their messages.

Built with
Python, Streamlit, Requests, Hugging Face API, Regex

Try it out

Live App: https://scam-message-detector-ej5cwpvzxvqqejfnfrofpu.streamlit.app/

Code Repo: https://github.com/manoj1-008/Scam-message-detector
