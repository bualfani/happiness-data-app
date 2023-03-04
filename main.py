import streamlit as st
import plotly.express as px

st.title("Happiness Data Graph")
st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
st.selectbox("Select The Data from the Y-axis")