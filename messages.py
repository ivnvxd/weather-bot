from weather import get_weather


def weather(latitude, longitude) -> str:
    """Returns a message about the temperature and weather description"""
    w = get_weather(latitude, longitude)
    return f'<b>{w.location}</b>\n' \
           f'\n' \
           f'<i>🌡 Temperature:</i> <b>{round(w.temp)}</b>°C, feels like <b>{round(w.feels_like)}</b>°C\n' \
           f'<i>🌤 Weather</i>: {w.weather_main}, {w.weather_description}\n' \
           f'<i>💨 Wind</i>: {w.wind_direction}, {w.wind_speed_description}, {w.wind_speed} m/s\n' \
           f'\n' \
           f'<i>🌄 Sunrise</i>: {w.sunrise.strftime("%H:%M")}\n' \
           f'<i>🌅 Sunset</i>: {w.sunset.strftime("%H:%M")}\n' \
           f'\n' \
           f'Have a nice day! ☺️'

           # f'<u>Max temp</u>:{round(w.temp_max)}°C, min temp: {round(w.temp_min)}°C\n' \
           # f'<u>Pressure</u>: {w.pressure}\n' \
