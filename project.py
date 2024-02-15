
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
    
    
    
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"  # Replace with your API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_current_weather(weather_data):
    if weather_data["cod"] == "200":
        print(f"Weather in {weather_data['city']['name']}:")
        current_weather = weather_data['list'][0]
        print(f"Temperature: {current_weather['main']['temp']}°C")
        print(f"Humidity: {current_weather['main']['humidity']}%")
        print(f"Wind Speed: {current_weather['wind']['speed']} m/s")
    else:
        print("City not found. Please enter a valid city name.")

def display_weather_forecast(weather_data):
    if weather_data["cod"] == "200":
        print(f"Weather forecast for {weather_data['city']['name']}:")
        for forecast in weather_data['list']:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weather_description = forecast['weather'][0]['description']
            print(f"{date}: {temperature}°C, {weather_description}")
    else:
        print("City not found. Please enter a valid city name.")

def main():
    print("Welcome to the Weather Forecast Application!")
    while True:
        city = input("Enter city name (or 'quit' to exit): ")
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        weather_data = get_weather(city)
        display_current_weather(weather_data)
        display_weather_forecast(weather_data)

if __name__ == "__main__":
    main()
