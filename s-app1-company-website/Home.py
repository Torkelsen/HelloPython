import streamlit as st
import pandas as pd
import lorem

st.set_page_config(layout="wide")

def create_employee_card(row):
    st.subheader(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
    st.write(row["role"])
    st.image("images/" + row["image"])

st.header("The Best Company")
st.write(" ".join(lorem.paragraph() for _ in range(3)))

st.subheader("Our Team")

df = pd.read_csv('data.csv', delimiter=',') #.set_index('ID') would cause i in the next for loop to be values from the ID col, not generated integer sequence
columns = st.columns(3)

for i, row in df.iterrows():
    col = columns[i % 3]  # Rotate through the 3 columns
    with col:
        create_employee_card(row)