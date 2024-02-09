import streamlit as st
from streamlit_gsheets import GSheetsConnection


url = "https://docs.google.com/spreadsheets/d/1WI0ZjnFvP1DQHTw0ujI7DtoQEAxBu0e-Q-9SqZPIleU/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1])
st.dataframe(data)

