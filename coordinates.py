from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_coordinates(lat, lon) -> Coordinates:
    """Returns current coordinates"""
    # latitude = 55.797199
    # longitude = 37.48953
    latitude = lat
    longitude = lon
    return Coordinates(latitude=latitude, longitude=longitude)
