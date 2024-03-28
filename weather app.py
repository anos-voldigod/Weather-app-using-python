##################################### WEATHER APP  #############################################
from tkinter import *
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
                
def update_weather():
      city = city_entry.get()
      weather_json = get_weather_data(city)
      if weather_json:
       weather_label.config(text=f"The weather in {city} is: {weather_json['weather'][0]['main']}")
       temp_label.config(text=f"Temperature: {round(weather_json['main']['temp'])}°F")
       humidity_label.config(text=f"Humidity: {weather_json['main']['humidity']}%")
       wind_label.config(text=f"Wind Speed: {weather_json['wind']['speed']} mph")
      else:
       weather_label.config(text="City Not Found!")
       
def main():
    city_input = input("Enter city: ")
    weather_json = get_weather_data(city_input)
    if weather_json:
        display_weather_info(weather_json, city_input)

window = Tk()
window.title("Weather App")

window.geometry("500x300") 

city_label = Label(window, text="Enter City:")
city_label.pack()

city_entry = Entry(window)
city_entry.pack()

get_weather_button = Button(window, text="Get Weather", command=update_weather)
get_weather_button.pack()

weather_label = Label(window, text="")
weather_label.pack()

temp_label = Label(window, text="")
temp_label.pack()

humidity_label = Label(window, text="")
humidity_label.pack()

wind_label = Label(window, text="")
wind_label.pack()

window.mainloop()

if __name__ == "__main__":
    main()
