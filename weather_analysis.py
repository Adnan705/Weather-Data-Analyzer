import pandas as pd
import numpy as np

# Sample weather data
data = {
    'Date': pd.date_range(start='2025-08-01', periods=7, freq='D'),
    'Temperature (C)': [34, 36, 32, 33, 35, 38, 31],
    'Humidity (%)': [45, 50, 55, 40, 60, 35, 50],
    'Wind Speed (km/h)': [10, 12, 8, 5, 20, 15, 10]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate averages
avg_temp = np.mean(df['Temperature (C)'])
avg_humidity = np.mean(df['Humidity (%)'])
avg_wind = np.mean(df['Wind Speed (km/h)'])

# Find hottest and coldest day
hottest_day = df.loc[df['Temperature (C)'].idxmax(), 'Date']
coldest_day = df.loc[df['Temperature (C)'].idxmin(), 'Date']

# Extreme weather detection
high_wind_days = df[df['Wind Speed (km/h)'] > 15]
low_humidity_days = df[df['Humidity (%)'] < 40]

# Print results
print("Average Temperature:", round(avg_temp, 2), "°C")
print("Average Humidity:", round(avg_humidity, 2), "%")
print("Average Wind Speed:", round(avg_wind, 2), "km/h")
print("\n Hottest Day:", hottest_day.date())
print(" Coldest Day:", coldest_day.date())
print("\n High Wind Days:\n", high_wind_days[['Date', 'Wind Speed (km/h)']])
print("\n Low Humidity Days:\n", low_humidity_days[['Date', 'Humidity (%)']])
