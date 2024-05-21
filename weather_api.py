import requests
import config

def what_weathe_in_city(city):
    # URL API сервиса OpenWeatherMap
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # Параметры запроса к API (например, название города и API ключ)
    params = {
        'q': f"{city}",
        'type': 'like',# Название города
        'units': 'metric',
        'lang': "ru",
        'appid': config.API  # Замените 'your_api_key_here' на ваш API ключ
    }

    # Выполняем GET-запрос к API
    response = requests.get(url, params=params)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Если запрос успешен, выводим полученные данные (например, в формате JSON)
        weather_data = response.json()
        description = f"Общее описание: {weather_data['weather'][0]['description']}"
        main_temp = f"Средняя температура:, {weather_data['main']['temp']}°C"
        humidity = f"Влажность: {weather_data["main"]["humidity"]}%"
        return description, main_temp, humidity
    else:
        # Если возникла ошибка, выводим сообщение об ошибке
        return f'Ошибка получения данных: {response.status_code}'

print(what_weathe_in_city(city="Москва"))
