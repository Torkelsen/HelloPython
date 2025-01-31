import streamlit as st
import os
import sys
# Add the parent directory (app2-portfolio) to sys.path
# TODO: this still give an error on line 6, but works run-time. Should be fixed
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import send_email
print("send_email module imported successfully!")  # Debugging check

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email")
    user_message = st.text_area("Your message")
    message = f"""\
Subject: New message from web form

from: {user_email}

{user_message}
"""
    button = st.form_submit_button("Send")
    if button:
        send_email.send_email(message)
        st.info("Your email was sent successfully")