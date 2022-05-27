import argparse

from services_data.exceptions import InputError
from services_data.technical_data import ServiceData


def user_request() -> tuple[str, int]:
    """get from the user city name and search radius of earthquakes"""

    parser = argparse.ArgumentParser(
        description="Earthquake counter",
        usage=ServiceData.usage
    )

    parser.add_argument("city", type=str, help="City name", nargs="*")
    parser.add_argument(
        "-r", "--radius",
        type=int,
        help=ServiceData.radius_description,
        default=1000,
    )

    namespace = parser.parse_args()
    city, radius = namespace.city, namespace.radius
    city = " ".join(city)   # if city contains more than one word

    if not city:
        raise InputError

    return city, radius
