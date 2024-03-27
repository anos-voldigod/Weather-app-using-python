##################################### WEATHER APP  #############################################

import requests

api_key = '67939fceaf40eb16692e78c698c3fa9b'

def get_weather_data(city):
    try:
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}"
        )
        weather_data.raise_for_status()  
        return weather_data.json()
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def display_weather_info(weather_json, city):
    if 'cod' in weather_json and weather_json['cod'] == '404':
        print("No City Found")
    else:
        weather = weather_json['weather'][0]['main']
        temp = round(weather_json['main']['temp'])
        humidity = weather_json['main']['humidity']
        wind_speed = weather_json['wind']['speed']

        print(f"The weather in {city} is: {weather}")
        print(f"The temperature in {city} is: {temp}ºF")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} mph")

def main():
    city_input = input("Enter city: ")
    weather_json = get_weather_data(city_input)
    if weather_json:
        display_weather_info(weather_json, city_input)

if __name__ == "__main__":
    main()


 






