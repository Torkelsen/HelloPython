import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

#def get_data(p_days):
#    dates = ["2025-07-02","2025-08-02","2025-09-02","2025-10-02","2025-11-02"]
#    temperatures = [10,11,12,18,14]
#    temperatures = [p_days * i for i in temperatures]
#    return  dates, temperatures

# TODO: filter data for date range
# TODO: Add Sky map

if len(place) > 0:
    data = get_data(place, days, "asd")
    figure = px.line(x=[entry["date_time"] for entry in data],y=[entry["temperature"] for entry in data], labels={"x": "Date", "y": "Temperature (C)"})
    st.plotly_chart(figure)