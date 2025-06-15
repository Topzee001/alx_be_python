import requests

API_KEY = "635728ed635d284b0a95a3634c3b8a0e"  # API key
LAT = 6.5244    # Latitude for Lagos
LON = 3.3792    # Longitude for Lagos

base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    temperature = data['main']['temp']  # Temperature in Kelvin
    weather_desc = data['weather'][0]['description']  # Weather description
    
    print(response)

    print(data)
    # temp_celsius = temperature - 273.15  # Convert Kelvin to Celsius
    
    # print(f"Current Temperature in Lagos: {temp_celsius:.2f}°C")
    # print(f"Weather Condition: {weather_desc}")
else:
    print("Error fetching weather data:", response.status_code)
