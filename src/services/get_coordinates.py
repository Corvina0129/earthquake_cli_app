from geopy import Nominatim

from services_data.technical_data import Coordinates
from services_data.exceptions import CantGetGPSCoordinates


def get_coordinates(city: str) -> Coordinates:
    """get coordinates by city name using geopy"""
    app = Nominatim(user_agent="some_user")
    try:
        location = app.geocode(city)
        return Coordinates(location.latitude, location.longitude)
    except (TypeError, AttributeError):
        raise CantGetGPSCoordinates
