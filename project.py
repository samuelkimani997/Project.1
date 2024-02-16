
# import requests

# def get_weather(city):
#     api_key = "YOUR_API_KEY"  # Replace with your API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
#     return data
# def display_weather(weather_data):
#     if weather_data["cod"] == 200:
#         print(f"Weather in {weather_data['name']}:")
#         print(f"Temperature: {weather_data['main']['temp']}°C")
#         print(f"Humidity: {weather_data['main']['humidity']}%")
#         print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
#     else:
#         print("City not found. Please enter a valid city name.")

# def main():
    
    
    
# import requests

# def get_weather(city):
#     api_key = "YOUR_API_KEY"  # Replace with your API key
#     url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
#     response = requests.get(url)
#     data = response.json()
#     return data

# def display_current_weather(weather_data):
#     if weather_data["cod"] == "200":
#         print(f"Weather in {weather_data['city']['name']}:")
#         current_weather = weather_data['list'][0]
#         print(f"Temperature: {current_weather['main']['temp']}°C")
#         print(f"Humidity: {current_weather['main']['humidity']}%")
#         print(f"Wind Speed: {current_weather['wind']['speed']} m/s")
#     else:
#         print("City not found. Please enter a valid city name.")

# def display_weather_forecast(weather_data):
#     if weather_data["cod"] == "200":
#         print(f"Weather forecast for {weather_data['city']['name']}:")
#         for forecast in weather_data['list']:
#             date = forecast['dt_txt']
#             temperature = forecast['main']['temp']
#             weather_description = forecast['weather'][0]['description']
#             print(f"{date}: {temperature}°C, {weather_description}")
#     else:
#         print("City not found. Please enter a valid city name.")

# def main():
#     print("Welcome to the Weather Forecast Application!")
#     while True:
#         city = input("Enter city name (or 'quit' to exit): ")
#         if city.lower() == 'quit':
#             print("Goodbye!")
#             break
#         weather_data = get_weather(city)
#         display_current_weather(weather_data)
#         display_weather_forecast(weather_data)

# if __name__ == "__main__":
#     main()




import requests

def get_weather_forecast(api_key, city):
    """
    Fetches weather forecast data from the OpenWeatherMap API.
    """
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Please try again later.")
        return None

def display_weather_forecast(forecast_data):
    """
    Displays the weather forecast for the next 5 days.
    """
    if forecast_data:
        print(f"Weather forecast for {forecast_data['city']['name']}:")
        for forecast in forecast_data['list']:
            date_time = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weather_description = forecast['weather'][0]['description']
            print(f"{date_time}: {temperature}°C, {weather_description}")
    else:
        print("No forecast data available.")

def save_forecast_to_file(forecast_data, filename):
    """
    Saves the weather forecast data to a file.
    """
    with open(filename, 'w') as file:
        file.write(str(forecast_data))

def load_forecast_from_file(filename):
    """
    Loads the weather forecast data from a file.
    """
    try:
        with open(filename, 'r') as file:
            forecast_data = eval(file.read())
        return forecast_data
    except FileNotFoundError:
        print("Forecast data file not found.")
        return None

def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    
    # Check if forecast data is available in a file
    filename = f"{city}_forecast.txt"
    forecast_data = load_forecast_from_file(filename)
    
    # If forecast data is not available in a file, fetch it from the API
    if forecast_data is None:
        forecast_data = get_weather_forecast(api_key, city)
        if forecast_data:
            save_forecast_to_file(forecast_data, filename)
    
    # Display the weather forecast
    display_weather_forecast(forecast_data)

if __name__ == "__main__":
    main()







