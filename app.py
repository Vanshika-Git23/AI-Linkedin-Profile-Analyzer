
import streamlit as st
import os
from pypdf import PdfReader
from google import genai

# Page configuration
st.set_page_config(
    page_title="LinkMind AI",
    page_icon="💼",
    layout="wide"
)

# Header
st.title("💼 LinkMind AI")
st.subheader("Your Intelligent LinkedIn Profile Coach")

st.write(
    "Analyze your LinkedIn profile and discover "
    "how to improve your professional presence."
)

st.divider()

# Input methods
method = st.radio(
    "How would you like to provide your profile?",
    [
        "Upload LinkedIn PDF",
        "Paste Profile Text",
        "LinkedIn Profile URL"
    ],
    horizontal=True
)

profile_text = ""
