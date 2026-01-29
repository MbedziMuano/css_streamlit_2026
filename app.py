import streamlit as st
import pandas as pd
from datetime import date

# ------------------ CSS FOR COLORS AND STYLING ------------------
st.markdown("""
<style>
/* Main background gradient */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #fce4ec);
}

/* Titles */
h1 {
    color: #0d47a1;
    text-align: center;
}
h2, h3 {
    color: #1a237e;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #263238;
}
[data-testid="stSidebar"] * {
    color: white;
}

/* Card style */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background-color: #1976d2;
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #0d47a1;
    color: #ffffff;
}

/* Success message */
.stAlert.success {
    background-color: #e8f5e9;
    color: #1b5e20;
}

/* Warning message */
.stAlert.warning {
    background-color: #fff3e0;
    color: #e65100;
}
</style>
""", unsafe_allow_html=True)

# ------------------ M


