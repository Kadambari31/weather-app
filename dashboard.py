import streamlit as st
import requests
import pandas as pd

API_KEY = "your_api_key_here"

st.title("🌦 Weather Data Dashboard")

city = st.text_input("Enter City Name", "Pune")

if st.button("Get Weather Data"):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    dates = []
    temperatures = []
    humidity = []

    for item in data["list"][:10]:
        dates.append(item["dt_txt"])
        temperatures.append(item["main"]["temp"])
        humidity.append(item["main"]["humidity"])

    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperatures,
        "Humidity": humidity
    })

    st.subheader("Temperature Chart")
    st.line_chart(df.set_index("Date")["Temperature"])

    st.subheader("Humidity Chart")
    st.bar_chart(df.set_index("Date")["Humidity"])