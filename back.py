import requests
import os 
from dotenv import load_dotenv

load_dotenv()
# Access environment variables
KEY_API = os.getenv("KEY_API")

def convert_to_celcius(temperature_in_kelvin):
    return temperature_in_kelvin-273.15

def get_coordonner(city_name):
    city_url = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={KEY_API}"
    response = requests.get(city_url)
    data = response.json()
    lat = data[0]['lat']
    long=data[0]['lon']
    return long, lat


def get_weather_data(long,lat):
    # Requête à une API de météo (remplacez l'URL par l'API réelle que vous souhaitez utiliser)
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={KEY_API}"
    response = requests.get(weather_url)
    weather_data = response.json()
    general = weather_data['weather'][0]['main']
    icon_id = weather_data['weather'][0]['icon']
    temperature = round(convert_to_celcius(weather_data['main']['temp']))
    max_temperature = round(convert_to_celcius(weather_data['main']['temp_max']))
    feels_temp = round(convert_to_celcius(weather_data['main']['feels_like']))
    humidity = weather_data['main']['humidity']
    icon = f'https://openweathermap.org/img/wn/{icon_id}@2x.png'
    return general, temperature, max_temperature, feels_temp, humidity, icon



