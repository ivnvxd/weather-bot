from urllib.request import urlopen
from dataclasses import dataclass
from datetime import datetime
from typing import Literal
import json
import ssl

# from wind import WindDirection
from coordinates import Coordinates
import config


@dataclass(slots=True, frozen=True)
class Weather:
    location: str
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    weather_main: str
    weather_description: str
    wind_speed: float
    wind_speed_description: str
    wind_direction: str
    sunrise: datetime
    sunset: datetime


def _get_openweather_response(latitude: float, longitude: float) -> str:
    """Gets Openweather response using API"""
    ssl._create_default_https_context = ssl._create_unverified_context
    url = config.OPENWEATHER_API_URL.format(latitude=latitude, longitude=longitude)
    return urlopen(url).read()


def _parse_openweather_response(openweather_response: str) -> Weather:
    """Parses Openweather response"""
    openweather_dict = json.loads(openweather_response)
    return Weather(
        location=_parse_location(openweather_dict),
        temp=_parse_temp(openweather_dict),
        feels_like=_parse_feels_like(openweather_dict),
        temp_min=_parse_temp_min(openweather_dict),
        temp_max=_parse_temp_max(openweather_dict),
        pressure=_parse_pressure(openweather_dict),
        weather_main=_parse_weather_main(openweather_dict),
        weather_description=_parse_weather_description(openweather_dict),
        wind_speed=_parse_wind_speed(openweather_dict),
        wind_speed_description=_wind_speed_description(openweather_dict),
        wind_direction=_parse_wind_direction(openweather_dict),
        sunrise=_parse_sun_time(openweather_dict, 'sunrise'),
        sunset=_parse_sun_time(openweather_dict, 'sunset')
    )


def get_weather(coordinates=Coordinates) -> Weather:
    """Requests the weather in OpenWeather API and returns it"""
    openweather_response = _get_openweather_response(
        longitude=coordinates.longitude, latitude=coordinates.latitude
    )
    weather = _parse_openweather_response(openweather_response)
    return weather


def _parse_location(openweather_dict: dict) -> str:
    return openweather_dict['name']


def _parse_temp(openweather_dict: dict) -> float:
    return openweather_dict['main']['temp']


def _parse_feels_like(openweather_dict: dict) -> float:
    return openweather_dict['main']['feels_like']


def _parse_temp_min(openweather_dict: dict) -> float:
    return openweather_dict['main']['temp_min']


def _parse_temp_max(openweather_dict: dict) -> float:
    return openweather_dict['main']['temp_max']


def _parse_pressure(openweather_dict: dict) -> int:
    return openweather_dict['main']['pressure']


def _parse_weather_main(openweather_dict) -> str:
    return str(openweather_dict['weather'][0]['main'])


def _parse_weather_description(openweather_dict) -> str:
    return str(openweather_dict['weather'][0]['description']).capitalize()


def _parse_sun_time(openweather_dict: dict, time: Literal["sunrise", "sunset"]) -> datetime:
    return datetime.fromtimestamp(openweather_dict['sys'][time])


def _parse_wind_speed(openweather_dict: dict) -> float:
    return openweather_dict['wind']['speed']


def _wind_speed_description(openweather_dict: dict) -> str:
    # TODO
    # speed = _parse_wind_speed(openweather_dict)

    pass


def _parse_wind_direction(openweather_dict: dict) -> str:
    degrees = openweather_dict['wind']['deg']
    degrees = round((degrees+10) / 22.5) * 22.5
    if degrees == 360:
        degrees = 0

    match degrees:
        case 0:
            direction = 'North'
        case 22.5:
            direction = 'North-Northeast'
        case 45:
            direction = 'Northeast'
        case 67.5:
            direction = 'East-Northeast'
        case 90:
            direction = 'East'
        case 112.5:
            direction = 'East-Southeast'
        case 135:
            direction = 'Southeast'
        case 157.5:
            direction = 'South-Southeast'
        case 180:
            direction = 'South'
        case 202.5:
            direction = 'South-Southwest'
        case 225:
            direction = 'Southwest'
        case 247.5:
            direction = 'West-Southwest'
        case 270:
            direction = 'West'
        case 292.5:
            direction = 'West-Northwest'
        case 315:
            direction = 'Northwest'
        case 337.5:
            direction = 'North-Northwest'

    return direction

