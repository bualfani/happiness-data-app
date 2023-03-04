import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Happiness Data Graph")
x = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y = st.selectbox("Select The Data from the Y-axis", ("GDP", "Happiness", "Generosity"))
st.subheader(f"{x} and {y}")

# loading the dataframe
df = pd.read_csv("happy.csv")

match x:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

match y:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.plotly_chart()