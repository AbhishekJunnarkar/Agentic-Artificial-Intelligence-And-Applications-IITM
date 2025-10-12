import requests


def get_weather(city_name, api_key):
    """
    Fetch current weather data for a given city using OpenWeatherMap API.

    Args:
        city_name (str): Name of the city
        api_key (str): Your OpenWeatherMap API key

    Returns:
        dict: Weather details (temperature, description, humidity, etc.)
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].title(),
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return {'error': 'City not found or invalid API key.'}

print(get_weather('Glasgow',''))