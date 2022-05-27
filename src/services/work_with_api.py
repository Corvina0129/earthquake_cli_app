import requests
from requests import JSONDecodeError

from services_data.exceptions import CantGetResponseFromApi
from services_data.technical_data import ServiceData


def get_response_from_api(
        latitude: float = 90,
        longitude: float = 90,
        radius: int = 1000
):
    """make a request to api, return the number of earthquakes"""
    resp = requests.get(ServiceData.URL.format(latitude, longitude, radius))
    try:
        count = resp.json()["count"]
    except JSONDecodeError:
        raise CantGetResponseFromApi

    return count
