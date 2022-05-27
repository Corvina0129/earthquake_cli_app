from datetime import datetime

from services_data.technical_data import Coordinates


def print_response(
        city: str,
        radius: int,
        latitude: Coordinates,
        longitude: Coordinates,
        count: int
):
    """returns a response to the user"""
    time = _current_time()
    print(f"""There are {count} earthquakes at {time}
             in {city.title()} by coordinates {latitude}:{longitude}
             on a radius of {radius} kilometers""")


def _current_time() -> str:
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time
