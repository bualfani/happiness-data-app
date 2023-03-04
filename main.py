import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Happiness Data Graph")
x_axis = st.selectbox("Select the data for the X-axis", ("GDP", "Happiness", "Generosity"))
y_axis = st.selectbox("Select The Data from the Y-axis", ("GDP", "Happiness", "Generosity"))

# loading the dataframe
df = pd.read_csv("happy.csv")

# x axis
match x_axis:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

# y axis
match y_axis:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

st.subheader(f"{x_axis} and {y_axis}")

# plotting the webpage
figure = px.scatter(x=x_array, y=y_array, labels={'x': x_axis, 'y': y_axis})
st.plotly_chart(figure)