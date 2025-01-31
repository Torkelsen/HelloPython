import os, sys
import streamlit as st
import pandas as pd
# Add the parent directory (app2-portfolio) to sys.path
# TODO: this still give an error on line 6, but works run-time. Should be fixed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from services import email_service

df = pd.read_csv('topics.csv')

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    user_topic = st.selectbox(
        "What topic do you want to discuss?",
        df["topic"])
    user_message = st.text_area("Your message")
    message = f"""\
Subject: New message from company project

from: {user_email}

topic: {user_topic}

{user_message}
    """
    submit_button = st.form_submit_button("Send")
    if submit_button:
        email_service.send_email(message)
        st.info("Your email was sent!")
        email_address = None
        message = None