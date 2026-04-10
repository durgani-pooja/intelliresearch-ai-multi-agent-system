import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

def get_groq_key():
    key = os.getenv("GROQ_API_KEY")
    if not key:
        key = st.secrets.get("GROQ_API_KEY")
    
    if not key:
        st.error("🔑 GROQ_API_KEY is missing! Ensure your .env file exists and contains GROQ_API_KEY=gsk_...")
        st.stop()
    return key