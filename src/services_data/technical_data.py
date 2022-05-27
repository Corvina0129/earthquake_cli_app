from dataclasses import dataclass
from enum import Enum
from typing import NamedTuple


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


@dataclass(frozen=True)
class ServiceData:
    URL = """https://earthquake.usgs.gov/fdsnws/event/1/count?format=geojson&latitude={}&longitude={}&maxradiuskm={}"""
    radius_description = """Limit to events within the specified maximum number of kilometers from the City."""
    usage = """Radius of search must be passed explicitly with -r or --radius (1000 km by default)"""


class Exceptions(str, Enum):
    COORDINATES_ERROR = "Can not get gps coordinate, enter city and radius again"
    API_ERROR = "Can not get response from api, enter city and radius again"
    INPUT_ERROR = "Input correct data please"
