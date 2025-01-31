import pandas
import streamlit as st
import pandas as pd
import sys

print(sys.path)
def create_project_card(df_row):
    st.header(df_row["title"])
    st.write(df_row["description"])
    st.image("images/" +row["image"])
    st.write(f"[Source Code]({row['url']})")

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", delimiter=';')



with col3:
    for index, row in df[:10].iterrows():
        create_project_card(row)


with col4:
    for index, row in df[10:].iterrows():
        create_project_card(row)
