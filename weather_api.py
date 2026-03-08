import requests
import pandas as pd
import matplotlib.pyplot as plt

# 🔑 Your API Key
API_KEY = "276f84984050b612b0d818f5b0f221ff"

# 🌍 City
city = "Pune"

# API URL
url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# Check API response
if data.get("cod") != "200":
    print("Error:", data)
else:
    print("API Connected Successfully ✅")

    # Extract date and temperature
    dates = []
    temperatures = []

    for item in data["list"][:10]:  # first 10 records
        dates.append(item["dt_txt"])
        temperatures.append(item["main"]["temp"])

    # Create DataFrame
    df = pd.DataFrame({
        "Date": dates,
        "Temperature": temperatures
    })

    print(df)

    # 📊 Plot Graph
    plt.figure()
    plt.plot(df["Date"], df["Temperature"])
    plt.xticks(rotation=45)
    plt.xlabel("Date & Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Forecast")
    plt.tight_layout()
    plt.show()