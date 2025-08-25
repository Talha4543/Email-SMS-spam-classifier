import streamlit as st
import pickle
import nltk
from nltk.stem.porter import PorterStemmer

# Load fitted pipeline
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title("📩 Email / SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):
    result = model.predict([input_sms])[0]

    if result == 1:
        st.header("🚨 Spam")
    else:
        st.header("✅ Not Spam")
