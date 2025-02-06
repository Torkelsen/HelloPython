import requests
import streamlit as st
import os

APIKEY = os.getenv("NASAOPENAPIKEY")
URL = "https://api.nasa.gov/planetary/apod"

response = requests.get(f"{URL}?api_key={APIKEY}")
content = response.json()
title = content["title"]
description = content["explanation"]
image_url = content["hdurl"]


st.header("Astronomy Image of the Day!")
st.subheader(str(title))
st.image(image_url)
st.text(description)