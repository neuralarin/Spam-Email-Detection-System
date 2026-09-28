import streamlit as st
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

# -----------------------------
# Load Model and Vectorizer
# -----------------------------
@st.cache_resource
def load_models():
    vectorizer = joblib.load("models/tfidf_vectorizer.pkl")
    model = joblib.load("models/spam_classifier_model.pkl")
    return vectorizer, model


vectorizer, model = load_models()

# -----------------------------
# App Title
# -----------------------------
st.title("📧 Spam Email Detection System")
st.write("Enter a message below to check whether it is **Spam** or **Not Spam**.")

st.divider()

# -----------------------------
# User Input
# -----------------------------
message = st.text_area(
    "Enter your email/message:",
    height=180,
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔍 Check Message", use_container_width=True):

    if message.strip() == "":
        st.warning("Please enter a message first.")

    else:
        # Transform message using TF-IDF
        message_vector = vectorizer.transform([message])

        # Prediction
        prediction = model.predict(message_vector)[0]

        st.divider()

        if prediction == 1:
            st.error("🚨 This mail is **SPAM**.")
        else:
            st.success("✅ This mail is **NOT SPAM**.")