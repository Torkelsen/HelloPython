import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Roger Torkelsen")
    content_info = """
    This project is for learning Python!
    """
    st.info(content_info)

content_description = """
Below you can find some of the apps i have built in Python
"""
st.write(content_description)