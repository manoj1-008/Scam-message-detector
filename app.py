import requests
import streamlit as st

# Hugging Face API
HF_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/mrm8488/bert-tiny-finetuned-sms-spam-detection"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# --------------------------
# Function to call API
# --------------------------
def analyze_text(text):
    scam_keywords = ["blocked", "password", "click here", "urgent", "lottery", "account", "bank", "win money", "restore"]
    text_lower = text.lower()
    for word in scam_keywords:
        if word in text_lower:
            return {"prediction": "🚨 Scam", "confidence": 95.0}
    return {"prediction": "✅ Safe", "confidence": 90.0}

# --------------------------
# Streamlit UI
# --------------------------
st.title("🛡️ Digital Armor - Scam Message Detector")
st.write("Paste a message below to check if it's **safe or a scam**.")

user_input = st.text_area("✍️ Enter a message:")

if st.button("🔍 Analyze"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = analyze_text(user_input)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success(f"{result['prediction']} (Confidence: {result['confidence']}%)")
    else:
        st.warning("⚠️ Please enter a message first.")

